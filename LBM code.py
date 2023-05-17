import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, animation
import time
import sys
np.set_printoptions(threshold=sys.maxsize)
start = time.perf_counter()

# Simulation Parameters
nx, ny = 400, 100 # number of cells
x, y = np.meshgrid(np.arange(nx), np.arange(ny))
nt = 31000  # timesteps
L = 9 #Number of directions
u0 = 0.12 # Initial Velocity
tau = 0.572 # Relaxation time
omega = 1 / tau # Relaxation Factor

# Obstacle Parameters
D = 20 # parameters for obstacle
h = nx/7
k = ny/2

# Non Used Parameters
nu = (2*tau-1)/6 # Kinematic Shear Viscosity
Re = (u0*D)/nu


# based upon D2Q9 structure
w = np.array([ 1/36, 1/9, 1/36, 1/9, 4/9, 1/9, 1/36, 1/9, 1/36]) # Weights of directions
e = np.array([ [ 1,  1], [ 1,  0], [ 1, -1], [ 0,  1], [ 0,  0],[ 0, -1], [-1,  1], [-1,  0], [-1, -1] ]) # Lattice velocities

def BoundaryConditions():

    rho[0, :] = (np.sum(fI[[3, 4, 5], 0, :], axis=0) + 2 * np.sum(fI[[6, 7, 8], 0, :], axis=0)) * (1 - u[0,0,:]) ** -1
    fI[[0, 1, 2], 0, :] = eq[[0, 1, 2], 0, :] + fI[[8, 7, 6], 0, :] - eq[[8, 7, 6], 0, :]

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
    circle = ((x - h) ** 2 + (y - k) ** 2 <= (D/2) ** 2)  # Creating a boolean matrix

# ##### Uncomment/Comment this section for animation (Takes long) ##################################
# Initialization()
# def update(nt):
#     global fI
#     fI,temp = StreamingnBounceBack()
#     u, rho = Macroscopic() #no problem
#     eq = Equilibrium(u,rho) # no problem
#     fI = fI -omega * (fI - eq) # no problem
#     fI[:, circle.T] = temp[:, circle.T]
#
#     if nt % 4 == 0:  # Update the animation every 4 frames
#         u_norm = np.linalg.norm(u, axis=0).T
#         imshow_obj.set_array(u_norm)
#         print(nt)
#         plt.clf()
#         return plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
#
# fig = plt.figure()
# imshow_obj = plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
# animation = animation.FuncAnimation(fig, update, interval=-100)
# plt.show()


#### Uncomment/Comment this section for static image #########################################
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
       print(f'Reynolds number = {Re} ')
       plt.clf()
       plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
       plt.show()







