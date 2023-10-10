# Function to find index of minimum
def indexOfMin(L, start, end):
    minIndex = start
    for i in range(start+1, end+1):
        if L[i] < L[minIndex]:
            minIndex = i
    return minIndex

L = [10, 4, 3, 7, 3, 15]

print(indexOfMin(L, 0, 5))
print(indexOfMin(L, 1, 5))
print(indexOfMin(L, 3, 4))
print(indexOfMin(L, 4, 4))