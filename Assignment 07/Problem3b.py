def fastIterativeModeFinder(L):
    low = 0
    high = len(L) - 1
    while high > low:
        mid = (low + high) // 2
        if L[mid+1] > L[mid]:
            low = mid + 1
        else:
            high = mid
    return low

L = [1]
print(fastIterativeModeFinder(L))
L =[50,2,1]
print(fastIterativeModeFinder(L))
L = [1,2,5,20]
print(fastIterativeModeFinder(L))
L = [1,2,4,7,11,10,8,4,-9]
print(fastIterativeModeFinder(L))
L = [-1, 0, 1, 2, -1]
print(fastIterativeModeFinder(L))