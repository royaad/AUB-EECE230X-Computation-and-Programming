from pa12Files.graph import UndirectedGraph 
import numpy

def adjacent(M,i,j): 
    """ Returns open neighbors of cell (i,j) in maze M
        Return value: list adj of tuples 
        Assumes i and j are in range """ 
    m = len(M)
    n = len(M[0])
    adjCells = []
    if i<m-1 and M[i+1][j]: # down
        adjCells.append((i+1,j))
    if j<n-1 and M[i][j+1]: # right
        adjCells.append((i,j+1))
    if i>0 and M[i-1][j]:  # up
        adjCells.append((i-1,j))  
    if j>0 and M[i][j-1]: # left
        adjCells.append((i,j-1))          
    return adjCells

def buildGraphFromMaze(M):
    m = len(M)
    n = len(M[0])
    G = UndirectedGraph()
    # build the graph using a for loop
    for i in range(m):
        for j in range(n):
            # check if the node is open
            if M[i][j]:
                # create the node
                G.addNode((i,j))
    # loop over the nodes
    for i,j in G.adj:
        tmp = adjacent(M,i,j)
        # loop over adjacent cells
        for adjcell in tmp:
            if adjcell not in G.adj[(i,j)]:
                G.connect((i,j),adjcell)
    return G

M = [[True, False, True],
    [True, True, True],
    [True, False, True]]
print("M:")
print(numpy.matrix(M,int))
print(adjacent(M,0,0))

G= buildGraphFromMaze(M)
print("G:")
print(G)