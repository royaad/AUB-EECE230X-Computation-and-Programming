from pa12Files.graph import UndirectedGraph 
import numpy

def buildGraphFromMaze(M):
    pass
            

M = [[True, False, True],
    [True, True, True],
    [True, False, True]]
print("M:")
print(numpy.matrix(M,int))
G= buildGraphFromMaze(M)
print("G:")
print(G)