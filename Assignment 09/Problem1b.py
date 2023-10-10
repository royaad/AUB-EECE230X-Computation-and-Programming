def equalElements(M):
    m = len(M)
    n = len(M[0])
    D = {}
    for i1 in range(m):
        for j1 in range(n):
            if M[i1][j1] not in D:
                D[M[i1][j1]] = [(i1, j1)]
            else:
                return (D[M[i1][j1]][0], (i1, j1))
    return ((-1, -1), (-1, -1))

import numpy as np
M1 = [[1,2],[3,4]]
M2 = [[1,2],[3,1]]
M3 = [[1,3,0,5],[2,5,2,-1],[5,6,-2,6]]
M4 = [[1,3,0,5],[20,50,2,-1],[51,61,-2,16]]
for M in (M1,M2,M3,M4):
    print(np.matrix(M))
    print(equalElements(M),"\n")

m=[[0], [-3], [-6], [3], [-2], [5], [5]]
print(equalElements(m))