import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


nx, ny = 400, 100   # number of cells
rho = 100    # density
nt = 4000   # timesteps
L = 9
nu = 0.08
omega = 1 / (3*nu+0.5)

# based upon D2Q9 structure
w = np.array([4 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 36, 1 / 36, 1 / 36, 1 / 36]) #weights of directions
e = np.array([[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1],[1, -1], [-1, 1]]) #lattice velocities


# Initialize grid, distribution function, equilibrium function
grid = np.zeros((L, nx, ny))
fI= np.zeros((L, nx, ny))
fO= np.zeros((L, nx, ny))
eq = np.zeros((L, nx, ny))
u = np.zeros((2,nx,ny))


#Macroscopic variables
rho = np.sum(fI,axis=0)
p = rho / 3
for i in range(L):
    u[0,:,:] =+ e[i,0]*fI[i,:,:]*rho**-1
    u[1, :, :] =+ e[i,1]*fI[i,:,:]*rho**-1

#Inflow and Outflow Boundary Conditions

fI[[4,6,8], -1, :] = fI[[4,6,8], -2, :] #Outflow

#Equlibrium
for i in range(L):
    eq[i,:,:] = rho * omega * (1 + 3 * (e[i,0]*u[0,:,:] + e[i,1]*u[1,:,:]) + 4.5 *(e[i,0]*u[0,:,:] + e[i,1]*u[1,:,:]) ** 2 - 1.5 *  (u[0]**2 + u[1]**2))

#Collision
fI = fO - omega * (fI-eq)

#Stream
for i in range(L):
    fI[i,:,:] = np.roll(np.roll(fI[i, :, :], e[i, 0], axis=0), e[i, 1], axis = 1)

#BounceBack
r = 5
h = ny/2
k = nx/6
x, y = np.meshgrid(np.arange(nx),np.arange(ny))
circle = ((x-h/2)**2 + (y-k/2)**2 <= r**2) # Creating a mask for the circle
circle.shape
for i in range(L):
    fO[i, circle.T] = fI[8-i, circle.T]



# animation
fig = pyplot.figure()
# Simulation = animation.FuncAnimation(fig,,)
pyplot.show()