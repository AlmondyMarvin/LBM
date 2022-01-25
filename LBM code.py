import numpy as np
from matplotlib import pyplot as plt


nx, ny = 400, 100   # number of cells
rho0 = 100    # density
tau = 0.6    # collision timescale
Nt = 4000   # timesteps
L = 9

# based upon D2Q9 structure
w = np.array([4 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 36, 1 / 36, 1 / 36, 1 / 36]) #weights of directions
e = np.array([[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1],[1, -1], [-1, 1]]) #lattice velocities

grid = np.zeros((nx,ny,L)) # Create the main grid which contains the 9 variables of each cell

fI = np.zeros((nx,ny,L))
fO = np.zeros((nx,ny,L))

def stream(L):
    for i in range (L):
        fI[i,:,:] = np.roll(np.roll(fO[i,:,:], e[i,0], axis=0), e[i,1] , axis = 1)

