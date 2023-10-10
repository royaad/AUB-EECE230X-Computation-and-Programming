# Get input from the user
n = int(input("Enter an integer n: "))

# Check if n is negative
if n < 0:
    print("Negative number!")
else:
    # Calculate the factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    # Display the result
    print(f"Factorial of n: {factorial}")