# Read and convert the first input sequence
input_sequence = input("Enter a sequence of integers separated by spaces: ")
L = [int(x) for x in input_sequence.split()]

# Set intial values
n = len(L)
maxSum = 0
current_sum = 0
a = 0
b = 0
c = 0
counter = 0

# Three nested loops
for i in range(n):
    # Compute sum using slicing
    current_sum += L[i]
    # Update current_sum, re-initialize a and b
    if current_sum < 0:
        current_sum = 0
        counter = 0
    # Keep track of the start in c in case of a new maxSum
    if counter == 0 and L[i] > 0:
        c = i
        counter += 1

    # In case of a new maxSum, update maxSum, a and b
    if current_sum > maxSum:
        maxSum = current_sum
        a = c
        b = i
    # print(i, L[i], counter,'\t',a, b, c, '\t', current_sum, maxSum)
# Print output
print('Max-sum = ', maxSum)
if maxSum:
    print("A max-sum subsequence:")
    for i in range(a, b + 1):
        print(L[i], end=' ')