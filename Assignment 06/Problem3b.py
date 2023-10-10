def binarySearchFirstOccurrence(L, x):
    n  = len(L)
    low = 0
    high = n-1
    while low<=high: 
        mid = (low+high)//2
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

def binarySearchLastOccurrence(L, x):
    n  = len(L)
    low = 0
    high = n-1
    while low<=high: 
        mid = (low+high)//2
        if L[mid] == x:
            if mid < n-1 and L[mid+1] == x:
                low = mid+1
            else:
                return mid
        elif L[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1         

def binarySearchFirstAndLastOccurrences(L, x):
    return (binarySearchFirstOccurrence(L, x), binarySearchLastOccurrence(L, x))

print(binarySearchFirstAndLastOccurrences([], 3))
print(binarySearchFirstAndLastOccurrences([5], 3))
print(binarySearchFirstAndLastOccurrences([5], 5))
print(binarySearchFirstAndLastOccurrences([3,5,5,5], 5))
print(binarySearchFirstAndLastOccurrences([3,5,5,5,5], 1))
print(binarySearchFirstAndLastOccurrences([3,5,5,5,5], 2))
print(binarySearchFirstAndLastOccurrences([3,5,7,7,7,15,26,30,33], 7))
print(binarySearchFirstAndLastOccurrences([3,5,7,7,7,15,26,30,33], 33))
print(binarySearchFirstAndLastOccurrences([3,5,7,7,7,15,26,30,33], 12))
print(binarySearchFirstAndLastOccurrences([3,3,5,7,15,26,30,33], 26))
print(binarySearchFirstAndLastOccurrences([3,3,3,3,3,3,3,3,3,3], 3))