# import sys
# print (sys.path)
from pa12Files.graph import buildGraphFromFile
from pa12Files.circularQueue import Queue
import matplotlib.pyplot as plt
# from Problem1b import buildGraphFromMaze
# will run the code and generate a Maze, we should use (if __name__ == "__main__") to avoid it.
    
def BFS(G,s,t):
    """ Breadth First Search function
    Assumes G is a directed or undirected graph and u is node in G
    Returns dict distance  mapping each node u (key) to the length of the  shortest 
    path from source s to u (value) 
    and dict parent mapping each node (key) to its parent (value) in shortest path to source """
    assert s in G.adj, "node not in graph"
    parent = {s:None} # Initialize dict parent
    distance = {s:0} # Initialize dict distance 
    # Initialize Q of max size the number of nodes in G: len(G.adj)
    Q = Queue(len(G.adj))
    Q.enqueue(s)
    while not Q.isEmpty():
    #        print("Q:", Q)
    #        print("distance:", distance)
    #        print("parent",  parent)
    #        print("--------")
        if t in distance and distance[t] != 0: return (distance,parent)
        u = Q.dequeue()
        for v in G.adj[u]:
            if v not in distance:
                distance[v]=distance[u]+1
                parent[v]=u
                Q.enqueue(v)
    return (distance,parent)

def extractPath(t,parent):
    L = []
    while t is not None:
        L.append(t)
        t = parent[t]
    L.reverse()
    return L

def findShortestPath(G,s,t):
    _, parent = BFS(G,s,t)
    print(parent)
    if t in parent:
        return extractPath(t,parent)
    else:
        return []

G = buildGraphFromFile("c:/Users/user/Desktop/AUB EECE230X/Assignment 12/pa12Files/UndirectedGraph2.txt", undirected =True)
# # UndirectedGraph2.txt is available in compressed folder associated with this assignment
# print(findShortestPath(G,'A','F'))
# print(findShortestPath(G,'A','I'))
# print(findShortestPath(G,'A','A'))
# plt.figure(1)
# plt.clf()
# G.draw()
# plt.show()

# # cases from sharifjudge
G.adj = {'a': ['a'], 'n': ['a']}
print(findShortestPath(G, s = 'n', t = 'n'))
plt.figure(1)
plt.clf()
G.draw()
plt.show()

G.adj = {'a': [], 'e': ['l'], 'v': ['a'], 'l': ['g', 'y'], 'x': ['y'], 'u': ['i'], 'p': [], 'g': [], 'd': ['p', 'v'], 'b': ['i'], 'q': ['q'], 'y': [], 'i': ['i', 'd']}
print(findShortestPath(G, s = 'e', t = 'e'))
plt.figure(1)
plt.clf()
G.draw()
plt.show()

G.adj = {'a': ['o'], 'p': [], 'q': [], 'o': ['a'], 'i': [], 'c': [], 'r': ['o']}
print(findShortestPath(G, s = 'p', t = 'p'))
plt.figure(1)
plt.clf()
G.draw()
plt.show()

G.adj = {'a': ['a', 'u'], 'u': ['a']}
print(findShortestPath(G, s = 'a', t = 'a'))
plt.figure(1)
plt.clf()
G.draw()
plt.show()

G.adj = {'a': ['a']}
print(findShortestPath(G, s = 'a', t = 'a'))
plt.figure(1)
plt.clf()
G.draw()
plt.show()

G.adj = {'a': []}
print(findShortestPath(G, s = 'a', t = 'a'))
plt.figure(1)
plt.clf()
G.draw()
plt.show()

# import numpy
# M=[[True, False, True, True, False, True, True],
# [True, True, False, True, True, False, False],
# [False, True, True, True, True, True, True],
# [False, True, True, False, False, False, True],
# [False, True, False, True, True, False, True]]
# print("M:")
# print(numpy.matrix(M,int))
# GMaze = buildGraphFromMaze(M)
# print(findShortestPath(GMaze,(0,0),(4,6)))
# plt.figure(2)
# plt.clf()
# GMaze.draw()
# plt.show()