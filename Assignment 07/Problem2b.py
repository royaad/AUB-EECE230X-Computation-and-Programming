def recPowerFast(x,n):
    """_summary_
    For n>=2, the recurrence is as follows:
    * The base function is for n == 2, we return x*x
    * For n > 2, we check if n is even then we call the recursive function for n/2 and we return x^(n/2)*x^(n/2)
    * If n is odd, we call the recursive function for n-1 and we return x*x^(n-1). n-1 is now necessarily even
    and the division by two is applied on the power function.
    """
    # print(n)
    if n == 0:
        return 1
    elif n > 0:
        if n%2:
            return x*recPowerFast(x, n-1)
        if n == 2:
            return x*x
        temp = recPowerFast(x, n//2)
        return temp*temp
    else:
        return 1/recPowerFast(x, -n)
    

# print("recPowerSlow(0,0):",recPowerFast(0,0))
# print("recPowerSlow(0,3):",recPowerFast(0,3))
# print("recPowerSlow(3,0):",recPowerFast(3,0))
# print("recPowerSlow(3,1):",recPowerFast(3,1))
# print("recPowerSlow(-3,1):",recPowerFast(-3,1))
# print("recPowerSlow(2,4):",recPowerFast(2,4))
# print("recPowerSlow(2,-4):",recPowerFast(2,-4))
# x = 1.25
# n = 82
# print(x,"**",n," :",x**n)
# print("recPower(",x,",",n,"):",recPowerFast(x,n))

# help(recPowerSlow)