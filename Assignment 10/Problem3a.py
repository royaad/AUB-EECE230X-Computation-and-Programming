def partition2(A,p,r):
    x = A[r]
    i1 = p-1
    i2 = p-1
    for j in range(p,r):
        if A[j]==x:
            i2+=1
            (A[i2],A[j])=(A[j],A[i2]) # Exchange A[i2] with A[j]
            # print(i1, i2, j)
            # print(L)
        elif A[j]<x:
            i1+=1
            i2+=1
            if i2==j:
                (A[i1],A[i2])=(A[i2],A[i1])
            elif i1==i2: # Not really necessary condition, less Exchange.
                (A[i1],A[j])=(A[j],A[i1])
            else:
                (A[i2],A[i1],A[j])=(A[i1],A[j],A[i2]) # Exchange A[i1] with A[i2], then A[i1] with A[j]
            # print(i1, i2, j)
            # print(L)
    i2+=1
    i1+=1
    (A[i2],A[r])=(A[r],A[i2])  # Exchange A[i2] with A[r]
    return (i1,i2)


L = [8, 9, 4, 8, 2, 3, 11, 1, 8, 10, 6, 7, 5, 8]
print(partition2(L, 0, len(L)-1))
print(L)

L = [65, 88, 65, 88, 58, 88, 58, 65, 58, 88]
print(partition2(L, 0, len(L)-1))
print(L)

L = [5, 6, 5, 5, 1, 3, 5, 2, 1, 7, 9, 5, 15, 100, 5, 2, 17, 5, 56]
print(partition2(L, 0, len(L)-1))
print(L)