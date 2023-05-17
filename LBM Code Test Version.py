import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, animation
import time
import sys
np.set_printoptions(threshold=sys.maxsize)

start = time.perf_counter()

nx, ny = 1000, 300  # number of cells
x, y = np.meshgrid(np.arange(nx), np.arange(ny))
nt = 3000  # timesteps
L = 9
u0 = 0.05 # Initial Velocity
r = ny//20 # parameters for obstacle
h = nx/6
k = ny/2
Re = 1000
nu = (u0*r)/Re
omega = 1 / ((3*nu)+0.5) # Relaxation Factor


# based upon D2Q9 structure
w = np.array([ 1/36, 1/9, 1/36, 1/9, 4/9, 1/9, 1/36, 1/9, 1/36]) # Weights of directions
e = np.array([ [ 1,  1], [ 1,  0], [ 1, -1], [ 0,  1], [ 0,  0],[ 0, -1], [-1,  1], [-1,  0], [-1, -1] ]) # Lattice velocities

def BoundaryConditions():


    rho[0, :] = (np.sum(fI[[3, 4, 5], 0, :], axis=0) + 2 * np.sum(fI[[6, 7, 8], 0, :], axis=0)) * (1 - u[0,0,:]) ** -1
    fI[[0, 1, 2], 0, :] = eq[[0, 1, 2], 0, :] + fI[[8, 7, 6], 0, :] - eq[[8, 7, 6], 0, :]

    # Zou - He Velocity Inlet BC

    # fI[1, 0, :] = (fI[7, 0, :] + 2 / 3 * rho[0, :] * u0)
    # fI[0, 0, :] = (fI[8, 0, :] - 1 / 2 * (fI[3, 0, :] - fI[5, 0, :]) + 1 / 6 * rho[0, :] * u0 )
    # fI[2, 0, :] = (fI[6, 0, :] + 1 / 2 * (fI[3, 0, :] - fI[5, 0, :]) + 1 / 6 * rho[0, :] * u0 )

    # Zou - He Pressure Outlet BC


    # Outlet
    fI[[0,1,2], -1, :] = fI[[0,1,2], -2, :]
    return fI, rho

def Macroscopic():
    rho = np.sum(fI, axis=0)
    u = np.zeros((2, nx, ny))
    for i in range(L):
        u[0, :, :] = u[0, :, :] + e[i, 0] * fI[i, :, :] * rho**-1
        u[1, :, :] = u[1, :, :] + e[i, 1] * fI[i, :, :] * rho**-1
    u[:, 0, :] = uini[:, 0, :]



    return u, rho

def Equilibrium(u, rho):
    eq = np.zeros((L, nx, ny))
    for i in range(L):
        uxe = e[i, 0] * u[0, :, :] + e[i, 1] * u[1, :, :]
        eq[i, :, :] = rho * w[i] * (1 + 3 * uxe + 4.5 * (uxe ** 2)- 1.5 * (u[0] ** 2 + u[1] ** 2))
    return eq

def StreamingnBounceBack():
    temp = fI
    temp[:, circle.T] = fI[::-1, circle.T]
    for i in range(L):
       fI[i, :, :] = np.roll(np.roll(fI[i, :, :], e[i, 0], axis=0), e[i, 1], axis=1)
    return fI,temp

def Initialization():
    global fI, eq, u, uini, rho, circle
    fI = np.zeros((L, nx, ny))
    eq = np.zeros((L, nx, ny))
    u = np.zeros((2, nx, ny))
    uini = u
    rho= np.ones((nx,ny))
    uini[0,:,:] = u0
    fI = Equilibrium(uini,rho)
    rho = np.sum(fI, axis=0)
    circle = ((x - h) ** 2 + (y - k) ** 2 <= r ** 2)  # Creating a boolean matrix

def getCoeff():
    Fx = [0]
    for k in range(nx):
        for j in range(ny):
            if circle[j, k] == True:
                # top
                tempvar = np.multiply(fI[:, j - 1, k], e[:, 0])
                tempvartwo = np.multiply(temp[:, j - 1, k], e[:, 0])
                Fx.extend([tempvar[w] for w in [6, 0]])
                Fx.extend([tempvartwo[w] for w in [6, 0]])
                break
    for k in reversed(range(nx - 1)):
        for j in reversed(range(ny - 1)):
            if circle[j, k] == True:
                # bottom
                tempvar = np.multiply(fI[:, j + 1, k], e[:, 0])
                tempvartwo = np.multiply(temp[:, j + 1, k], e[:, 0])
                Fx.extend([tempvar[w] for w in [8, 2]])
                Fx.extend([tempvartwo[w] for w in [8, 2]])
                break
    for j in range(ny):
        for k in range(nx):
            if circle[j, k] == True:
                # right
                tempvar = np.multiply(fI[:, j, k - 1], e[:, 0])
                tempvartwo = np.multiply(temp[:, j, k - 1], e[:, 0])
                Fx.extend([tempvar[w] for w in [6, 7, 8]])
                Fx.extend([tempvartwo[w] for w in [6, 7, 8]])
                break

    for j in reversed(range(ny - 1)):
        for k in reversed(range(nx - 1)):
            if circle[j, k] == True:
                # left
                tempvar = np.multiply(fI[:, j, k + 1], e[:, 0])
                tempvartwo = np.multiply(temp[:, j, k + 1], e[:, 0])
                Fx.extend([tempvar[w] for w in [0, 1, 2]])
                Fx.extend([tempvartwo[w] for w in [0, 1, 2]])
                break
    Fx = np.sum(Fx)
    Cd = Fx / (r * u0 * u0)  # rho = 1
    print(f'Drag Coefficient and Fx are equal to {Cd} and {Fx} respectively')

# ##### Uncomment/Comment this section for animation (Takes long) ##################################
# Initialization()
# def update(nt):
#     global fI
#     fI,temp = StreamingnBounceBack()
#     u, rho = Macroscopic() #no problem
#     eq = Equilibrium(u,rho) # no problem
#     fI = fI -omega * (fI - eq) # no problem
#     fI[:, circle.T] = temp[:, circle.T]
#     print(nt)
#     plt.clf()
#     return plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
#
#
#
# fig = plt.figure()
# plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
# animation = animation.FuncAnimation(fig, update, interval=0)
# plt.show()


##### Uncomment/Comment this section for static image #########################################
Initialization()
for i in range(nt):
    fI,temp= StreamingnBounceBack()
    u, rho = Macroscopic()
    fI, rho = BoundaryConditions()
    eq = Equilibrium(u,rho)
    fI = fI -omega * (fI - eq)
    fI[:, circle.T] = temp[:, circle.T]
    print(i)
    if i>nt-2:
       dudx, dudy = np.gradient(u[0, :, :], nx, ny)
       dvdx, dvdy = np.gradient(u[1, :, :], nx, ny)
       vorticity = dvdx - dudx
       print(f'Finished {i} iterations  in {time.perf_counter() - start} seconds')
       getCoeff()
       plt.clf()
       plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
       plt.show()







