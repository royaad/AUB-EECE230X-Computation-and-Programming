# Read and convert the first input sequence
input_sequence1 = input("Enter the first sequence of integers separated by spaces: ")
L1 = [int(x) for x in input_sequence1.split()]

# Read and convert the second input sequence
input_sequence2 = input("Enter the second sequence of integers separated by spaces: ")
L2 = [int(x) for x in input_sequence2.split()]

# Check if the lengths of L1 and L2 are equal
if len(L1) != len(L2):
    print("NO: Second sequence is not a permutation of the first")
# Check if L2 is a permutation of L1
else:
    found = [False]*len(L1)
    for i in range(len(L1)):
        for j in range(len(L2)):
            if L1[i] == L2[j]:
                L2[j] = 'X'  # Mark as crossed
                found[i] = True
                break
    if False in found:
        print("NO: Second sequence is not a permutation of the first")
    else:
        print("YES: Second sequence is a permutation of the first")