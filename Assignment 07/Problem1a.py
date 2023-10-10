def f(n):
    global N
    N += 1
    if n <= 2:
        return 1
    return f(n-1) + f(n-2) + f(n-3) + f(n//3)

print("f(n) for n = 0...9:")
for i in range(10):
    N=0
    print(f(i), end=" ")

N=0
print("\nf(25): ",f(25))
print("Number of recursive calls for 25:", N)