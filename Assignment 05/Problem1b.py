def wordSearch(fileName, word):
    # Open file
    h = open(fileName, 'r')
    line_count = 1
    line_found = 0
    for line in h:
        # Check if word is in line
        if word in line:
            line_found = line_count
            break
        line_count += 1
    # Close file
    h.close()
    return line_found
    

# Call function
# filename = 'C:/Users/user/Desktop/AUB/Assignment 05/test.txt'
print(wordSearch('test.txt', 'test'))