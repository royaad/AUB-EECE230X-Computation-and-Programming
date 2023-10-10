def fIterative(n):
    if n <= 2:
        return 1
    previous1 = previous2 = previous3 = 1
    templist = [1]*(n//3+1)
    # This loop fills all the needed divisions
    for i in range(3, n//3+1):
        # print(i)
        (previous1, previous2, previous3) = (previous1+previous2+previous3+templist[i//3], previous1, previous2)
        templist[i] = previous1
    # This loops carries on with the calculations / no need to store anymore
    print(templist)
    for i in range(max(3,n//3+1), n+1):
        # print(i)
        (previous1, previous2, previous3) = (previous1+previous2+previous3+templist[i//3], previous1, previous2)
    return previous1

# print("f(n) for n = 0...9:")
# for i in range(10):
#     print(fIterative(i), end=" ")

print("\nf(25): ",fIterative(4))
