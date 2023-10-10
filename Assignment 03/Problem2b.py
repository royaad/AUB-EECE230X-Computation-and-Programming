# Read and convert the first input sequence
input_sequence1 = input("Enter the first sequence of integers separated by spaces: ")
L1 = [int(x) for x in input_sequence1.split()]

# Read and convert the second input sequence
input_sequence2 = input("Enter the second sequence of integers separated by spaces: ")
L2 = [int(x) for x in input_sequence2.split()]

# Check if the sequences are identical
are_identical = L1 == L2

# Print the result
if are_identical:
    print("Sequences are equal")
else:
    print("Sequences are not equal")