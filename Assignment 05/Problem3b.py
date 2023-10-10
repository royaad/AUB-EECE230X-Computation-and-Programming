def generatePrimes(n):
    B = [True]*n
    count = 2
    while count**2 <= n:
        if B[count] == True:
            
            for i in range(count**2, n, count):
                B[i] = False
       
        count += 1
    P = []
    for i in range(2, n):
        if B[i]:
            P.append(i)
    return (P, B)

def primesCount(n):
    (_,B)=generatePrimes(n)
    count = [0]*n
    i = 2
    while i < n:
        if B[i]:
            count[i] = count[i-1] + 1
        else:
            count[i] = count[i-1]
        i += 1
    return count
        
print(primesCount(5))
print(primesCount(10))