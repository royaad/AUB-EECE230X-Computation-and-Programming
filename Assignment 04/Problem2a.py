# Initiate sequence
L = [5, 2, 4, 6, 1, 3]

# Initiate state
n = len(L) - 1

for i in range(n):
    minIndex = i
    for j in range(i+1, n+1):
        if L[j] < L[minIndex]:
            minIndex = j
    (L[i], L[minIndex]) = (L[minIndex], L[i])
    print(L)