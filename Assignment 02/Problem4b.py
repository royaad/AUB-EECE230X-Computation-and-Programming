# Part b

n = int(input("Enter an integer n: "))

if n < 0:
    print(f"{n} is not a square")
elif n == 0:
    print(f"YES square: {n} = 0^2")
else:
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        
        if square == n:
            print(f"YES square: {n} = {mid}^2")
            break
        elif square < n:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print(f"{n} is not a square")