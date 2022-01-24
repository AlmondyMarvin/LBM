import numpy as np
from matplotlib import pyplot as plt


Nx = 100    # dicretizaion of x , this is a rectangle
Ny = 25    # dicretizaion of y
rho0 = 100    # density
tau = 0.6    # collision timescale
Nt = 4000   # timesteps

# based upon D2Q9 structure
w = np.array([4 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 36, 1 / 36, 1 / 36, 1 / 36]) #weights of directions
e = np.array([[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1],[1, -1], [-1, 1]]) #indices of each direction

print(e)