# Roy Aad

def threeDistinct(L):
    if len(L) < 3: return False
    def threeDistinctRecursive(L, count, low, high):
        if (high - low) <= 1:
            if L[high] != L[low]:
                return count + 1
            else:
                return count
        if L[low] == L[high]:
            return count
        else:
            mid = (low + high)//2
            count = threeDistinctRecursive(L, count+1, low, mid)
            return threeDistinctRecursive(L, count, mid+1, high)

    return threeDistinctRecursive(L, 0, 0, len(L)-1) >= 2

print(threeDistinct([]))
print(threeDistinct([1]))
print(threeDistinct([1,1]))
print(threeDistinct([1,10]))
print(threeDistinct([1,1,10]))
print(threeDistinct([1,2,10]))
print(threeDistinct([1,1,10,10,10]))
print(threeDistinct([1,1,3,10,10,10]))
print(threeDistinct([1,1,3,10,10,10,10,10,10]))
print(threeDistinct([1,1,1,1,1,3,3,4,10]))
print(threeDistinct([10,10,10,21,21]))
print(threeDistinct([10,10,10,16,21,21]))
print(threeDistinct([10,10,10,16,21,21]))