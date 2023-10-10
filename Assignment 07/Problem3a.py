def recursiveModeFinder(L, low, high):
    # print(low, high)
    if low >= high:
        return low
    mid = (low + high) // 2
    # if low and high are consecutive mid == low
    # in its most fundemental case, when we can a list of 2 elements the mode is the max of both
    if L[mid+1] > L[mid]:
        return recursiveModeFinder(L, mid+1, high)
    else:
        return recursiveModeFinder(L, low, mid)



L = [1]
print(recursiveModeFinder(L, 0, len(L)-1))
L =[50,2,1]
print(recursiveModeFinder(L, 0, len(L)-1))
L = [1,2,5,20]
print(recursiveModeFinder(L, 0, len(L)-1))
L = [1,2,4,7,11,10,8,4,-9]
print(recursiveModeFinder(L, 0, len(L)-1))
L = [-1, 0, 1, 2, -1]
print(recursiveModeFinder(L, 0, len(L)-1))
