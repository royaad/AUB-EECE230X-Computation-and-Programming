def generatePrimes(n):
    # Create Boolean list with all True
    B = [True]*n
    # Change B[0] nad B[1] to False
    # B[0] = B[1] = False
    # Initiate a count at 2 since 2 will be the smallest prime
    count = 2
    # The non-prime numbers can be checked within sqrt of n
    # For example 2, 3, 4, 5, 6, 7, 8, 9
    # 2 and 3 check suffices to check non-primes 4, 6, 8, and 9
    while count**2 <= n:
        if B[count] == True:
            # Loop over multiples of count and change condition
            for i in range(count**2, n, count):
                B[i] = False
        # Move to next number
        count += 1
    # Create empty list to append primes
    P = []
    for i in range(2, n):
        if B[i]:
            P.append(i)
    return (P, B)

(P,B)=generatePrimes(0)
print(P)
(P,B)=generatePrimes(10)
print(P)
(P,B)=generatePrimes(20)
print(P)
(P,B)=generatePrimes(1000)
print(P)