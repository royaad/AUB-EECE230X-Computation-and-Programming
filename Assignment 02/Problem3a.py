# Part a

n = int(input("Enter n: "))

if n <= 1:
    print(n, "is not prime")
else:
    isPrime = True
    d = 2

    while d * d <= n:
        if n % d == 0:
            isPrime = False
            break
        d = d + 1
    
    if isPrime:
        print(n, "is prime")
    else:
        print(n, "is not prime")