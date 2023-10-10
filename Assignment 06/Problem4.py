def merge(L, R):
    m = len(L)
    n = len(R)
    i = j = 0
    C = []
    if m == 0 or n == 0:
        C = L + R
    else:
        while i < m and j < n:
            # print(m, i,n, j)
            if L[i] <= R[j]:
                C.append(L[i])
                i += 1
            else:
                C.append(R[j])
                j += 1
        if i == m:
            C += R[j:]
        if j == n:
            C += L[i:]
    return C

print(merge([1,3,5,7,9],[2,4,6,8,10]))
print(merge([1,5,7],[2,3,5,8,9,9]))
print(merge([1,5,7],[20,30,50,80,90,90]))
print(merge([10,50,70],[2,3,5,8,9,9]))
print(merge([1,5,7],[]))
print(merge([],[2,3,5,8,9,9]))
print(merge([1,2,3],[1,2,3]))