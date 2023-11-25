# Roy Aad 

def allStable(L):
    L.sort()
    n = len(L)
    for i in range(0,n-1,2):
        if L[i+1]-L[i] > 5: return False
    return True

print(allStable([75,70]))
print(allStable([75,69]))
print(allStable([100,70,96,73]))
print(allStable([100,70,90,73]))
print(allStable([100,80,70,96,73,75]))
print(allStable([100,82,70,96,73,75]))