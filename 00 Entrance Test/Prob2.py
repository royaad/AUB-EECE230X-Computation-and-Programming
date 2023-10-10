n = int(input("Enter n: "))

sequence = []

for i in range(n):
    sequence.append(n - i%2)
    
print(sequence)