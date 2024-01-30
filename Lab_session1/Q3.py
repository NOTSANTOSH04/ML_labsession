import numpy as np

def power_of_matrix(matrix, m):
    return np.linalg.matrix_power(matrix, m)

n = int(input(" Enter the matrix dimension:"))
matrix = np.random.randint(0,10,(n,n))
m = int(input("Enter the power:"))
result = power_of_matrix(matrix, m)
print(result)