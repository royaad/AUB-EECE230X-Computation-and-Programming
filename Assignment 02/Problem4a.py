# Part a

n = int(input("Enter an integer n: "))

if n < 0:
    print(f"{n} is not a square")
else:
    x = 0
    while x * x <= n:
        if x * x == n:
            print(f"YES square: {n} = {x}^2")
            break
        x += 1
    else:
        print(f"{n} is not a square")