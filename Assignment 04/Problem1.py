# Read input string from the user
input_string = input("Enter a string: ")

# Initiate state
isPalindrome = True
n = len(input_string)

for i in range(n//2):
    if input_string[i] != input_string[-1-i]:
        isPalindrome = False
        break

# Print the result
if isPalindrome:
    print("YES palindrome")
else:
    print("NOT a palindrome")