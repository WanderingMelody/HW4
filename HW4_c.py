import numpy as np
from scipy.linalg import lu_factor, lu_solve
"""
Utilized ChatGPT
"""

# Define 3x3 matrix and its corresponding identity matrix
matrix_3x3 = np.array([
    [3, 1, -1],
    [1, 4, 1],
    [2, 1, 2]
])
identity_3x3 = np.array([2, 12, 10])

# Define 4x4 matrix and its corresponding identity matrix
matrix_4x4 = np.array([
    [1, -10, 2, 4],
    [3, 1, 4, 12],
    [9, 2, 3, 4],
    [-1, 2, 7, 3]
])
identity_4x4 = np.array([2, 12, 21, 37])

def solve_matrices(matrix, identity):
    """
    Check code-supplied functions for size and then solves the provided matrices.  Utilizes numpy linear algebra for 3x3
    and scipy LU factorization code for 4x4
    :param matrix: Code-supplied matrix
    :param identity: Code-supplied identity matrix
    :return: Roots of code-supplied matrices
    """
    size = matrix.shape[0]
    if size == 3:
        roots = np.linalg.solve(matrix, identity)
    elif size == 4:
        lu, piv = lu_factor(matrix)
        roots = lu_solve((lu, piv), identity)
    else:
        raise ValueError("Matrix size must be 3x3 or 4x4")
    return roots

def main():
    """
    Finds the Roots of the two matrices.
    Uses NumPy for the 3x3 Matrix
    Uses SciPy for the 4x4 Matrix
    """
    roots_3x3_numpy = solve_matrices(matrix_3x3, identity_3x3)
    roots_4x4_scipy = solve_matrices(matrix_4x4, identity_4x4)
    print("Roots of the 3x3 matrix using NumPy:")
    print(roots_3x3_numpy)
    print("\nRoots of the 4x4 matrix using SciPy:")
    print(roots_4x4_scipy)

if __name__ == "__main__":
    main()