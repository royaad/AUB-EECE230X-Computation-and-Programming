# Read and convert the first input sequence
input_sequence = input("Enter a sequence of integers separated by spaces: ")
L = [int(x) for x in input_sequence.split()]

# Set intial values
n = len(L)
maxSum = 0
a = 0
b = 0

# Three nested loops
for i in range(n):
    for j in range(i,n):
        current_sum = 0
        for k in range(i, j+1):
            current_sum += L[k]
        # Update maxSum, a, and b
        if current_sum > maxSum:
            maxSum = current_sum
            a = i
            b = j

# Print output
print('Max-sum = ', maxSum)
if maxSum:
    print("A max-sum subsequence:")
    for i in range(a, b + 1):
        print(L[i], end=' ')