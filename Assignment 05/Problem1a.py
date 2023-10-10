def isWordInFile(fileName, word):
    # Open file
    h = open(fileName, 'r')
    # Read string
    s = h.read()
    # Close file
    h.close()
    # Check if word is in string
    if word in s:
        return True
    else:
        return False

# Call function
# filename = 'C:/Users/user/Desktop/AUB/Assignment 05/test.txt'
print(isWordInFile('test.txt',"Programming"))