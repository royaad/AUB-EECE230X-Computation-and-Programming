def binarySearch(L, x):
    n  = len(L)
    low = 0
    high = n-1
    while low<=high: 
        mid = (low+high)//2
        if L[mid] == x: 
            return mid
        elif L[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1

def sorted2Sum(L, t):
    for i in L:
        ans = binarySearch(L, t-i)
        if ans != -1:
            return True
    return False

L = [-6, 1, 3, 5, 7, 8, 9, 11]

print(sorted2Sum(L, 14)) # 7+7
print(sorted2Sum(L, 12)) # 1+11
print(sorted2Sum(L, 15)) # 7+8
print(sorted2Sum(L, 3)) # -6+9
print(sorted2Sum(L, 0))
print(sorted2Sum(L, 7))
print(sorted2Sum(L, 21))