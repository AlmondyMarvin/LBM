import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation


nx, ny = 400, 100   # number of cells
rho = 100    # density
nt = 4000   # timesteps
L = 9
nu = 0.08
omega = 1 / (3*nu+0.5)
u0 = 0.04
r = 5
h = ny / 2
k = nx / 6
x, y = np.meshgrid(np.arange(nx), np.arange(ny))

# based upon D2Q9 structure
w = np.array([4 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 36, 1 / 36, 1 / 36, 1 / 36]) #weights of directions
e = np.array([[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1],[1, -1], [-1, 1]]) #lattice velocities


# Initialize grid, distribution function, equilibrium function
grid = np.zeros((L, nx, ny))
fI= np.zeros((L, nx, ny))
fO= np.zeros((L, nx, ny))
eq = np.zeros((L, nx, ny))
u = np.zeros((2,nx,ny))



#Initialization to avoid getting NaN
u[1,:,:] = 0
u[0,:,:] = u0*(1-(y.T**2/(ny**2/4)))
rho = 1
for i in range(9):
    fI[i,:,:]= rho * omega * (1 + 3 * (e[i, 0] * u[0, :, :] + e[i, 1] * u[1, :, :]) + 4.5 * (e[i, 0] * u[0, :, :] + e[i, 1] * u[1, :, :]) ** 2 - 1.5 * (u[0] ** 2 + u[1] ** 2))



#main loop
for t in range(nt):

    # Outflow
    fI[[4, 6, 8], -1, :] = fI[[4, 6, 8], -2, :]

    # Macroscopic variables calculation
    rho = np.sum(fI, axis=0)
    for i in range(L):
        u[0, :, :] = + e[i, 0] * fI[i, :, :] * rho ** -1
        u[1, :, :] = + e[i, 1] * fI[i, :, :] * rho ** -1


    rho[0,:] = 1/(1-u[0,0,:]) * (sum(fI[[2,1,3],0,:]) +2*sum(fO[[4,6,8],0,:]) )


    # Equlibrium
    for i in range(L):
        eq[i, :, :] = rho * omega * (1 + 3 * (e[i, 0] * u[0, :, :] + e[i, 1] * u[1, :, :]) + 4.5 * (
                    e[i, 0] * u[0, :, :] + e[i, 1] * u[1, :, :]) ** 2 - 1.5 * (u[0] ** 2 + u[1] ** 2))

    # Collision
    fI = fO - omega * (fI - eq)

    # BounceBack
    circle = ((x - h / 2) ** 2 + (y - k / 2) ** 2 <= r ** 2)  # Creating a boolean matrix
    for i in range(L):
        fO[i, circle.T] = fI[8 - i, circle.T]

    # Stream
    for i in range(L):
        fI[i, :, :] = np.roll(np.roll(fI[i, :, :], e[i, 0], axis=0), e[i, 1], axis=1)

    if t == 20:
        print (u)
    plt.clf()
    plt.imshow(np.linalg.norm(u,axis=0).T, cmap=cm.viridis)
    plt.show()




# animation
fig = plt.figure()
# Simulation = animation.FuncAnimation(fig,,)
