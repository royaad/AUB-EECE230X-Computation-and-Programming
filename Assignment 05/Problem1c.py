def duplicateLines(fileName):
    # Check if extension is or not txt
    name = fileName.split('.')[:-1]
    name = ''.join(name)
    extension = '.' + fileName.split('.')[-1]
    assert extension == '.txt', 'File extension is not .txt'
    # Open file
    h = open(fileName, 'r')
    # Open duplicate file
    hDuplicate = open(name+'Duplicated'+extension,'w')
    for line in h:
        if line.endswith('\n'):        
            hDuplicate.write(2 * line)
        else:
            hDuplicate.write(line+'\n'+line)

    # Close files
    h.close()
    hDuplicate.close()

# Call function
#filename = 'C:/Users/user/Desktop/AUB/Assignment 05/test.txt'
#duplicateLines(filename)