def concatenateHorizontal(A,B):
    temp = []
    n = len(A)
    for i in range(n):
        temp.append(A[i] + B[i])
    return temp

import numpy
A = [[1, 2, 3],[4, 5, 6]]
B = [[7, 8, 9 ], [10, 11, 12]]
C = A+B
D = concatenateHorizontal(A,B)
print("A:")
print(numpy.matrix(A))
print("\nB:")
print(numpy.matrix(B))
print("\nC:")
print(numpy.matrix(C))
print("\nD:")
print(numpy.matrix(D))