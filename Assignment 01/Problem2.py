# Store repeated substrings in variables
line1 = "The wheels on the bus go "
line2 = "round and round,\n"
line3 = "all through the town."

# Build the final string using concatenation and repetition
s = line1 + (3* line2) + line1 + line2 + line3

# Print the result
print(s)