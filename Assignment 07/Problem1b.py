def fMemoized(n):
    def f(n):
        global N
        N += 1
        if L[n] != -1:
            return L[n]
        elif n <= 2:
            L[n] = 1
        else:
            L[n] = f(n-1) + f(n-2) + f(n-3) + f(n//3)
        return L[n]
    
    L = [-1]*(n+1)
    return f(n)

print("f(n) for n = 0...9:")
for i in range(10):
    N=0
    print(fMemoized(i), end=" ")

N=0
print("\nf(25): ",fMemoized(25))
print("Number of recursive calls for 25:", N)