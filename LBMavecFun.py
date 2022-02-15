import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import cm,animation

start = time.perf_counter()

nx, ny = 200, 40   # number of cells
nt = 2000  # timesteps
L = 9
u0 = 0.12
Re=400
r = 3
h = nx/6
k = ny/2
nu = (u0*r)/Re
nu=0.005
omega = 1 / ((3*nu)+0.5)
x, y = np.meshgrid(np.arange(nx), np.arange(ny))

# based upon D2Q9 structure
w = np.array([ 1/36, 1/9, 1/36, 1/9, 4/9, 1/9, 1/36, 1/9, 1/36]) #weights of directions
e = np.array([ [ 1,  1], [ 1,  0], [ 1, -1], [ 0,  1], [ 0,  0],[ 0, -1], [-1,  1], [-1,  0], [-1, -1] ]) #lattice velocities



#def initialization():
    # Initialize grid, distribution function, equilibrium function
#    global fI, fO, eq, u, uini, rho



def macroscopic():
    rho = np.sum(fI, axis=0)
    u = np.zeros((2, nx, ny))
    for i in range(L):
        u[0, :, :] = u[0, :, :] + e[i, 0] * fI[i, :, :] * rho**-1
        u[1, :, :] = u[1, :, :] + e[i, 1] * fI[i, :, :] * rho**-1
    u[:, 0, :] = uini[:, 0, :]
    rho[0, :] = (np.sum(fI[[3, 4, 5], 0, :], axis=0) + 2 * np.sum(fI[[6, 7, 8], 0, :], axis=0)) * (1 - u0) ** -1
    return u, rho


def equilibrium(u,rho):
    eq = np.zeros((9, nx, ny))
    for i in range(9):
        uxe = e[i, 0] * u[0, :, :] + e[i, 1] * u[1, :, :]
        eq[i, :, :] = rho * w[i] * (1 + 3 * uxe + 4.5 * (uxe ** 2)- 1.5 * (u[0] ** 2 + u[1] ** 2))
    return eq

def streamingncollision():
    for i in range(L):
        fO[i, circle.T] = fI[8-i, circle.T]
    for i in range(L):
       fI[i, :, :] = np.roll(np.roll(fO[i, :, :], e[i, 0], axis=0), e[i, 1], axis=1)
    return fO, fI

fI = np.zeros((L, nx, ny))
fO = np.zeros((L, nx, ny))
eq = np.zeros((L, nx, ny))
u = np.zeros((2, nx, ny))
circle = ((x - h) ** 2 + (y - k) ** 2 <= r ** 2)  # Creating a boolean matrix
uini=u
rho=np.ones((nx,ny))
uini[0,:,:]=0.12
uini[1,:,:]=0
fI = equilibrium(uini, 1)
rho = np.sum(fI, axis=0)
# initialization()



dudx, dudy = np.gradient(uini[0, :, :], nx, ny)
dvdx, dvdy = np.gradient(uini[1, :, :], nx, ny)
vorticitynot = dvdx - dudx


def update(nt):
    global fI,fO
    # startupdate = time.perf_counter()
    fI[[6,7,8], -1, :] = fI[[6,7,8], -2, :]
    u, rho = macroscopic()
    u[:, 0, :] = uini[:, 0, :]
    eq = equilibrium(u,rho)
    fI[[0,1,2],0,:] = eq[[0,1,2],0,:] + fI[[8,7,6],0,:] - eq[[8,7,6],0,:]
    fO = fI - omega*(fI - eq)
    fO,fI = streamingncollision()
    # finishupdate = time.perf_counter()
    # print(finishupdate - startupdate)
    print(nt)
    plt.clf()
    dudx, dudy = np.gradient(u[0, :, :], nx, ny)
    dvdx, dvdy = np.gradient(u[1, :, :], nx, ny)
    vorticity = dvdx - dudx
    return plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)



# for i in range (nt):
#     fI[[6, 7, 8], -1, :] = fI[[6, 7, 8], -2, :]
#     u, rho = macroscopic()
#     u[:, 0, :] = uini[:, 0, :]
#     rho[0, :] = 1 / (1 - u[0, 0, :]) * (np.sum(fI[[3, 4, 5], 0, :], axis=0) + 2 * np.sum(fI[[6, 7, 8], 0, :], axis=0))
#     eq = equilibrium(u, rho)
#     fI[[0, 1, 2], 0, :] = eq[[0, 1, 2], 0, :] + fI[[8, 7, 6], 0, :] - eq[[8, 7, 6], 0, :]
#     fO = fI - omega * (fI - eq)
#     fO, fI = streamingncollision()
#
#
#
#     if i>1500:
#         dudx, dudy = np.gradient(u[0, :, :], nx, ny)
#         dvdx, dvdy = np.gradient(u[1, :, :], nx, ny)
#         vorticity = dvdx - dudx
#         print(time.perf_counter() - start)
#         plt.imshow(vorticity.T, cmap=cm.viridis)
#         plt.colorbar()
#         plt.show()






fig = plt.figure()

plotty = plt.imshow(np.linalg.norm(uini,axis=0).T, cmap=cm.viridis)
animation = animation.FuncAnimation(fig, update,frames=nt,  interval=0.001)
cbar = plt.colorbar()
plt.show()

