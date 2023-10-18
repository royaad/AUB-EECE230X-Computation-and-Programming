# import sys
# print (sys.path)
from pa12Files.graph import BFS, buildGraphFromFile 
import matplotlib.pyplot as plt
from Problem1b import buildGraphFromMaze

def extractPath(t,parent):
    L = []
    while t is not None:
        L.append(t)
        t = parent[t]
    L.reverse()
    return L

def findShortestPath(G,s,t):
    _, parent = BFS(G,s)
    if t in parent:
        return extractPath(t,parent)
    else:
        return []

G = buildGraphFromFile("c:/Users/user/Desktop/AUB EECE230X/Assignment 12/pa12Files/UndirectedGraph2.txt", undirected =True)
# UndirectedGraph2.txt is available in compressed folder associated with this assignment
plt.figure(1)
plt.clf()
G.draw()
plt.show()
print(findShortestPath(G,'A','F'))
print(findShortestPath(G,'A','I'))

import numpy
M=[[True, False, True, True, False, True, True],
[True, True, False, True, True, False, False],
[False, True, True, True, True, True, True],
[False, True, True, False, False, False, True],
[False, True, False, True, True, False, True]]
print("M:")
print(numpy.matrix(M,int))
GMaze = buildGraphFromMaze(M)
plt.figure(2)
plt.clf()
GMaze.draw()
plt.show()
print(findShortestPath(GMaze,(0,0),(4,6)))