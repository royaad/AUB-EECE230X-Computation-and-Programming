# Read and convert the first input sequence
input_sequence1 = input("Enter the first sequence of integers separated by spaces: ")
L1 = [int(x) for x in input_sequence1.split()]

# Read and convert the second input sequence
input_sequence2 = input("Enter the second sequence of integers separated by spaces: ")
L2 = [int(x) for x in input_sequence2.split()]

# Check if the sequences are identical
are_identical = True

if len(L1) != len(L2):
    are_identical = False
else:
    for i in range(len(L1)):
        if L1[i] != L2[i]:
            are_identical = False
            break

# Print the result
if are_identical:
    print("Sequences are equal")
else:
    print("Sequences are not equal")