# Read the number of integers
n = int(input("Enter the number of integers: "))

# Initialize variables
prev = None
isSorted = True

for i in range(n):
    # Read the user input
    x = int(input("Enter an integer: "))
    
    # Compare x with prev
    if i > 0 and x < prev:
        isSorted = False
        break
    
    # Update prev
    prev = x

# Print the result
if isSorted:
    print("YES: input is sorted")
else:
    print("NO: input is not sorted")