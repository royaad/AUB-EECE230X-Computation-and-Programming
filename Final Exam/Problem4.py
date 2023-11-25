def threeDistinct(L):
    def threeDistinctRecursive(L, count, last_value):
        # Check if count is bigger than 3
        if count >= 3: return True
        # Check if L is empty and return False
        if not L: return False
        # Check if last value is different and increment count
        if L[0] != last_value:
            return threeDistinctRecursive(L[1:], count + 1, L[0])
        else:
            return threeDistinctRecursive(L[1:], count, L[0])

    return threeDistinctRecursive(L, 0, None)

print(threeDistinct([]))
print(threeDistinct([1]))
print(threeDistinct([1,1]))
print(threeDistinct([1,10]))
print(threeDistinct([1,1,10]))
print(threeDistinct([1,1,10,10,10]))
print(threeDistinct([1,1,3,10,10,10]))
print(threeDistinct([1,1,3,10,10,10,10,10,10]))
print(threeDistinct([1,1,1,1,1,3,3,4,10]))
print(threeDistinct([10,10,10,21,21]))
print(threeDistinct([10,10,10,16,21,21]))
print(threeDistinct([10,10,10,16,21,21]))