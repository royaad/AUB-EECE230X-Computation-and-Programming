# Part b

x = int(input("Enter x: "))

count_primes = 0

for num in range(2, x + 1):
    
    is_prime = True
    d = 2
    
    while d * d <= num:
        if num % d == 0:
            is_prime = False
            break
        d = d + 1

    if is_prime:
        count_primes += 1
        
print(count_primes)

fraction = count_primes / x
print(f"Fraction of primes less than or equal to {x} : {fraction}")