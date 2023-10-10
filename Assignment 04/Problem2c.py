# Function to find index of minimum
def indexOfMin(L, start, end):
    minIndex = start
    for i in range(start+1, end+1):
        if L[i] < L[minIndex]:
            minIndex = i
    return minIndex

def selectionSort(L):
    n = len(L) - 1
    for i in range(n):
        minIndex = indexOfMin(L, i, n)
        (L[i], L[minIndex]) = (L[minIndex], L[i])

# Read and convert the input sequence
# input_sequence = input("Enter a sequence of integers separated by spaces: ")
# L = [int(x) for x in input_sequence.split()]
L = [2, 1]
selectionSort(L)
print(L)