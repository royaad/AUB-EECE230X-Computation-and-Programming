# Roy Aad

def oneStable(L):
    L.sort()
    n = len(L)
    if n < 2 : return False
    for i in range(n-1):
        if L[i+1]-L[i] <= 5: return True
    return False

print(oneStable([]))
print(oneStable([75]))
print(oneStable([75,70]))
print(oneStable([75,69]))
print(oneStable([75,70,100]))
print(oneStable([85,70,100]))
print(oneStable([100,70,90, 73,96]))
print(oneStable([105,63,90, 70,96]))