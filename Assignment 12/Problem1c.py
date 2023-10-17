from pa12Files.graph import DiGraph, buildGraphFromFile
import matplotlib.pyplot as plt

def transpose(G):
    GTranspose = DiGraph()
    for node1 in G.adj:
        GTranspose.addNode(node1)
    for node1 in G.adj:
        for node2 in G.adj[node1]:
            GTranspose.connect(node2,node1)
    return GTranspose

G = buildGraphFromFile("c:/Users/user/Desktop/AUB EECE230X/Assignment 12/pa12Files/DiGraph1.txt", undirected = False)
# DiGraph1.txt is available in compressed folder associated with this assignment
plt.figure(1)
plt.clf()
G.draw()
plt.show()
GTranspose = transpose(G)
plt.figure(2)
plt.clf()
GTranspose.draw()
plt.show()