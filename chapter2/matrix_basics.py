import numpy as np


def section():
    print('----------------------------')


A = np.arange(16).reshape((4, 4))
print(A)
section()

# upper-left sub-matrix
print(A[0:2, 0:2])
section()
# upper-right sub-matrix
print(A[0:2, 2:4])
section()
# lower-left sub-matrix
print(A[2:4, 0:2])
section()
# lower-right sub-matrix
print(A[2:4, 2:4])
section()

print()

# matrix transpose
print('A')
print(A)
section()
print('Transpose of A')
print(A.T)
section()
B = np.arange(16, 32).reshape((4, 4))
print('B')
print(B)
section()
print('Transpose of B')
print(B.T)

print()

# properties of matrix transpose
print('A^T + B^T')
print(A.T + B.T)
section()
print('(A+B)^T')
print((A + B).T)

print()

print('(AB)^T')
print(np.dot(A, B).T)
section()
print('B^T * A^T')
print(np.dot(B.T, A.T))

print()
