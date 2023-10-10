def insertionSort(L):
    n = len(L)
    for j in range(1,n):
        # Insert L[j] into the sorted sequence  L[0∙∙∙j-1]
        key = L[j] # Save L[j] in key to avoid loosing it 
        i = j-1
        while  i>=0 and L[i] > key: 
                L[i+1] = L[i]  # move L[i] forward 
                i = i -1       # and go one step back
        L[i+1] = key

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

def fast3Sum(L, t):
    insertionSort(L)
    for i in L:
        if linearSorted2Sum(L, t-i):
            return True
    return False

L = [-6, 1, 3, 5, 7, 9, 11]
print(fast3Sum(L,2)) # e.g., -6+1+7
print(fast3Sum(L,5)) # e.g., 1+1+3
print(fast3Sum(L,7)) # e.g., 1+1+5
print(fast3Sum(L,15)) # e.g., 1+3+11
print(fast3Sum(L,19)) # e.g., 3+7+9
print(fast3Sum(L,0))
print(fast3Sum(L,1))
print(fast3Sum(L,18))
print(fast3Sum(L,20))
print(fast3Sum(L,28))