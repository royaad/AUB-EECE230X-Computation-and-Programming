def concatenateHorizontal(A, B):
    temp = []
    n = len(A)
    for i in range(n):
        temp.append(A[i] + B[i])
    return temp

def generatePattern(k):
    if k == 0: return [[1]]
    A = generatePattern(k-1)
    n = 2 ** (k-1)
    B = [[0]*n]*n
    return concatenateHorizontal(A, A) + concatenateHorizontal(B, A)

import numpy
for k in range(5):
    print("k=",k,":")
    print(numpy.matrix(generatePattern(k)),"\n")
    
# For fun: show matrix as a figure with 1 and 0 in different colors
import matplotlib.pyplot as plt
plt.imshow(generatePattern(10))
plt.show()