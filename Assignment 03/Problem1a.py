# Read input sequence from the user
input_sequence = input("Enter integers separated by spaces: ")

# Convert input sequence into a list of integers
sequence_list = [int(x) for x in input_sequence.split()]

# Check if the list is sorted in increasing order
isSorted = True
for i in range(1, len(sequence_list)):
    if sequence_list[i] < sequence_list[i - 1]:
        isSorted = False
        break

# Print the result
if isSorted:
    print("YES: input is sorted")
else:
    print("NO: input is not sorted")