def elementDistinctnessFast(L):
    n = len(L)
    if n < 2:
        return True
    L_copy = L.copy()
    L_copy.sort()
    i = 0
    is_Distinct = True
    while i < n-1:
        if L_copy[i] == L_copy[i+1]:
            return False
        else:
            i += 1
    return is_Distinct

print(elementDistinctnessFast([1,2,5,10,3,31,32,33,37,50,250]))
print(elementDistinctnessFast([1,2]))
print(elementDistinctnessFast([1]))
print(elementDistinctnessFast([]))
print(elementDistinctnessFast([1,2,5,2,10]))
print(elementDistinctnessFast([10,1,2,10]))
print(elementDistinctnessFast([1,2,5,10,3,31,32,33,37,5,250]))
print(elementDistinctnessFast([2,2]))