import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, animation
import time

start = time.perf_counter()

nx, ny = 200, 40   # number of cells
nt = 50000  # timesteps
L = 9
u0 = 0.12
r = 3
h = nx/6 # parameters for obstacle
k = ny/2
nu = 0.005
omega = 1 / ((3*nu)+0.5)


# based upon D2Q9 structure
w = np.array([ 1/36, 1/9, 1/36, 1/9, 4/9, 1/9, 1/36, 1/9, 1/36]) #weights of directions
e = np.array([ [ 1,  1], [ 1,  0], [ 1, -1], [ 0,  1], [ 0,  0],[ 0, -1], [-1,  1], [-1,  0], [-1, -1] ]) #lattice velocities


def Macroscopic():
    rho = np.sum(fI, axis=0)
    u = np.zeros((2, nx, ny))
    for i in range(L):
        u[0, :, :] = u[0, :, :] + e[i, 0] * fI[i, :, :] * rho**-1
        u[1, :, :] = u[1, :, :] + e[i, 1] * fI[i, :, :] * rho**-1
    u[:, 0, :] = uini[:, 0, :]
    rho[0, :] = (np.sum(fI[[3, 4, 5], 0, :], axis=0) + 2 * np.sum(fI[[6, 7, 8], 0, :], axis=0)) * (1 - u0) ** -1
    return u, rho

def Equilibrium(u, rho):
    eq = np.zeros((9, nx, ny))
    for i in range(9):
        uxe = e[i, 0] * u[0, :, :] + e[i, 1] * u[1, :, :]
        eq[i, :, :] = rho * w[i] * (1 + 3 * uxe + 4.5 * (uxe ** 2)- 1.5 * (u[0] ** 2 + u[1] ** 2))
    fI[[0, 1, 2], 0, :] = eq[[0, 1, 2], 0, :] + fI[[8, 7, 6], 0, :] - eq[[8, 7, 6], 0, :]
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
    x, y = np.meshgrid(np.arange(nx), np.arange(ny))
    rho=np.ones((nx,ny))
    uini[0,:,:]=u0
    fI = Equilibrium(uini,rho)
    rho = np.sum(fI, axis=0)
    circle = ((x - h) ** 2 + (y - k) ** 2 <= r ** 2)  # Creating a boolean matrix

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
    fI,temp = StreamingnBounceBack()
    u, rho = Macroscopic() #no problem
    eq = Equilibrium(u,rho) # no problem
    fI = fI -omega * (fI - eq) # no problem
    fI[:, circle.T] = temp[:, circle.T]
    print(i)

    if i>15000:
       dudx, dudy = np.gradient(u[0, :, :], nx, ny)
       dvdx, dvdy = np.gradient(u[1, :, :], nx, ny)
       vorticity = dvdx - dudx
       print(f'Finished {i} iterations  in {time.perf_counter() - start} seconds')
       plt.clf()
       plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
       plt.show()



