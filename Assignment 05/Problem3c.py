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
        
import matplotlib.pyplot as plt
from math import log

n = [i for i in range(2, 200)]
fun = [i/log(i) for i in n]
pcount = [primesCount(i)[-1] for i in n]

plt.figure(1)
plt.plot(n, pcount, 'r', label = 'pi(i)')
plt.plot(n, fun, 'k', label = 'i/log(i)')
plt.xlabel('i')
plt.legend()
plt.title('Density of primes')
plt.show()