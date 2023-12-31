from pa12Files.graph import buildGraphFromFile 
import matplotlib.pyplot as plt

def DFSVisitModified(G,u,index,count):
    # add the starting node to the component
    index[u]=count
    # loop over connected nodes
    for v in G.adj[u]:
        # if not visited yet, to avoid getting stuck in cycles
        if v not in index:
            # add the connected node to the component iteratively
            DFSVisitModified(G,v,index,count)

def findConnectedComponents(G):
    index = {}
    count = 0
    # looping over all nodes
    for u in G.adj:
        # check if node is not visited yet
        if u not in index:
            DFSVisitModified(G,u,index,count)
            count += 1
    # creating a list of lists from the dictionary
    # first create an empty list
    L = [[] for _ in range(count)]    # we can equally use L=list([[]*count]*count)
    # iterating over keys and values for index dictionnary
    for k, v in index.items():
        L[v].append(k)
    return L

G = buildGraphFromFile("c:/Users/user/Desktop/AUB EECE230X/Assignment 12/pa12Files/UndirectedGraph3.txt", undirected =True)
print(G)
plt.figure(2)
plt.clf()
G.draw()
plt.show()
print(findConnectedComponents(G))
G = buildGraphFromFile("c:/Users/user/Desktop/AUB EECE230X/Assignment 12/pa12Files/UndirectedGraph1.txt", undirected =True)
plt.figure(1)
plt.clf()
G.draw()
plt.show()
print(findConnectedComponents(G))
G = buildGraphFromFile("c:/Users/user/Desktop/AUB EECE230X/Assignment 12/pa12Files/UndirectedGraph4.txt", undirected =True)
plt.figure(3)
plt.clf()
G.draw()
plt.show()
print(findConnectedComponents(G))