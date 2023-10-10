def linearSorted2Sum(L, t): 
    i = 0
    j = len(L) - 1
    # print(t)
    while j >= i:
        # print(i, j, L[i]+L[j])
        if L[i]+L[j] == t:
            return True
        elif L[i]+L[j] < t:
            i += 1
        else:
            i -= 1
            i = max(0, i)
            j -= 1
    return False

L = [-6, 1, 3, 5, 7, 8, 9, 11]

print(linearSorted2Sum(L, 14)) # 7+7
print(linearSorted2Sum(L, 12)) # 1+11
print(linearSorted2Sum(L, 15)) # 7+8
print(linearSorted2Sum(L, 3)) # -6+9
print(linearSorted2Sum(L, 0))
print(linearSorted2Sum(L, 7))
print(linearSorted2Sum(L, 21))