n = int(input("Enter a number: "))

path = [n]

divisio = n

while divisio > 0:
    modulo = divisio%10
    divisio = divisio//10
    #print(divisio)
    #print(modulo)
    path.append(divisio)
    if (modulo != 3) and (modulo != 7):
        path = [0]
        break
    
print(sum(path))