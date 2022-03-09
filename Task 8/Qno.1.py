import numpy as np
S = np.array([8,9,10,11,12])
nz = 5
P = np.zeros(len(S) + (len(S)-1)*(nz))
P[::nz+1] = S
print(P)