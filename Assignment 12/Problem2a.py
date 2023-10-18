from pa12Files.graph import DFSVisit, buildGraphFromFile 
import matplotlib.pyplot as plt

def extractPath(t,parent):
    L = []
    while t is not None:
        L.append(t)
        t = parent[t]
    L.reverse()
    return L

def findAPath(G,s,t):
    parent = {s:None}
    DFSVisit(G,s,parent)
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
print(findAPath(G,'A','F'))
print(findAPath(G,'A','I'))