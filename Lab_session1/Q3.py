import numpy as np

def power_of_matrix(matrix, m):            #numpy matrix power function
    return np.linalg.matrix_power(matrix, m)

n = int(input(" Enter the matrix dimension:"))
matrix = np.random.randint(0,10,(n,n))            #creation of random matrix of dimension n*n
m = int(input("Enter the power:"))
result = power_of_matrix(matrix, m)              #function call
print(result)