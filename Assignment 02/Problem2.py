n = int(input("Enter the number 'n' of integers: "))

seq = []

for i in range(n):
    seq.append(int(input(f"Enter integer {i+1}: ")))

print(seq)

if n == 0:
    print("Empty sequence")
else:
    maximum = seq[0]
    i = 1

    while i < n:
        x = seq[i]
        if x > maximum:
            maximum = x
        i += 1

    print("Maximum:", maximum)