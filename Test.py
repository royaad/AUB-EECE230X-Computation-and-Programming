from math import pi

x = 0.1

y = x**2
print(y)

x = 1
y = x
x = 2
print(x,y)

for i in range(5,0,-1):
    for j in range(1,i):
        print(j, end=' ')
    print(i)
    
from copy import deepcopy
L0 = [0]
L = [L0, L0]
L1 = L
L2 = L.copy()
L3 = deepcopy(L)
print(id(L0))
print(id(L[0]))
print(id(L1[0]))
print(id(L2[0]))
print(id(L3[0]))