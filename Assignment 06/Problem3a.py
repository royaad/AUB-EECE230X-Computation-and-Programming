def binarySearchFirstOccurrence(L, x):
    n  = len(L)
    low = 0
    high = n-1
    while low<=high: 
        mid = (low+high)//2
        # print(x, mid)
        if L[mid] == x:
            if mid > 0 and L[mid-1] == x:
                high = mid-1
            else:
                return mid
        elif L[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1         

print(binarySearchFirstOccurrence([5], 5))
print(binarySearchFirstOccurrence([3,5,5,5], 5))
print(binarySearchFirstOccurrence([3,5,7,7,7,15,26,30,33], 7))
print(binarySearchFirstOccurrence([3,3,3,3,3,3,3,3,3,3], 3))