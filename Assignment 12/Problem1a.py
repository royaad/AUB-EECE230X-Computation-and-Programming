from pa12Files.graph import UndirectedGraph 
import matplotlib.pyplot as plt

def buildCircleGraph(n):
    assert n>=3, "n should be bigger or equal to 3"
    G = UndirectedGraph()
        
    for i in range(n):
        G.addNode(i+1)
        
    if n%2 == 0:
        print("Even")
        for i in range(0,n,2):
            if i>0:
                G.connect(i+1,i)
                G.connect(i+1,i+2)
            else:
                G.connect(i+1,i+2)
                G.connect(i+1,n)
    else:
        print("Odd")
        for i in range(0,n,2):
            if i==0:
                G.connect(i+1,i+2)
            elif i<n-1:
                G.connect(i+1,i)
                G.connect(i+1,i+2)
            else:
                G.connect(i+1,i)        
                G.connect(i+1,1)       
    return G
            

G= buildCircleGraph(17)
print(G)
plt.figure(1)
plt.clf()
G.draw()
plt.show()