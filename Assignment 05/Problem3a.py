def generatePrimes(n):
    # I don't need to append
    # I can simply remove elements
    P = [i for i in range(2, n)]
    B = [False]*n
    count = 1

    for i in P:
        B[i] = True
        for j in P[count:]:
            if j%i == 0:
                P.remove(j)
        count += 1
    
    return (P, B)

(P,B)=generatePrimes(2)
print(P)
(P,B)=generatePrimes(10)
print(P)
(P,B)=generatePrimes(20)
print(P)
(P,B)=generatePrimes(100)
print(P)