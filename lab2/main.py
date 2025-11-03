import numpy as np

mat1 = np.arange(1, 31)
mat1 = np.reshape(mat1, (6, 5))
print(mat1, end="\n---- ---- ---- ----\n")

# Q1
print(mat1[2:4, :2], end="\n---- ---- ---- ----\n")
# Q2
print(mat1[[0, 1, 2, 3], [1, 2, 3, 4]], end="\n---- ---- ---- ----\n")
# Q3
print(mat1[[0, 4, 5], 3:])
