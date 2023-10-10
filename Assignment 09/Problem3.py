def longestZeroSumSubList(L):
    n = len(L)
    sum = 0
    D = {0: 0}
    length = 0
    temp_L = []
    for i in range(n):
        sum += L[i]
        if sum not in D:
            D[sum] = i + 1
        else:
            temp_i = D[sum]
            temp_length = i + 1 - temp_i
            if temp_length > length:
                length = temp_length
                temp_L = L[D[sum]:i+1]
    return temp_L
            
print(longestZeroSumSubList([1, 10, -1, -1, 2, 3, -5, 26]))
print(longestZeroSumSubList([1 ,10, -1, -1, 4, 3, -5, 26]))
print(longestZeroSumSubList([1, 10, 1, -1, 4, 3, -5, 26]))
print(longestZeroSumSubList([1, 10, 1, 0, 4, 3, -5, 26]))
print(longestZeroSumSubList([1, 10, 1, 1, 4, 3, -5, 26]))
print(longestZeroSumSubList([-1, -1, 2, 3, -5, 26]))
print(longestZeroSumSubList([2, 2, -1, 0, -1, 2]))
print(longestZeroSumSubList([1, 0, -2, 1, 0, 1, -1, 0, -1, 2, -2, -2]))
print(longestZeroSumSubList([-1, -1, 2, 3, 5, 26]))
print(longestZeroSumSubList([0]))

