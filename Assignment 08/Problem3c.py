def fourSumFast(L,t):
    def linearSorted2Sum(L,t):  #O(n)
        """ assumes L is sorted"""
        n = len(L)
        i = 0
        j = n-1
        while i<= j: 
            if L[i]+L[j]==t: 
                return True
            elif L[i]+L[j]>t:  
            # Decrement j since adding  L[j] to another element in the range i...j 
            # could only make the sum larger  
                j-=1
            else: # i.e., if  L[i]+L[j]<t 
            # Increment i since adding  L[i] to another element in the range i...j 
            # could only make the sum smaller  
                i+=1
        return False
    n = len(L)
    L_new = []
    for i in range(n):
        for j in range(i,n):
            L_new.append(L[i]+L[j])
    L_new.sort()

    return linearSorted2Sum(L_new, t)

L = [13, 5, 7, 9, 112,16,27,31]
print(fourSumFast(L,24)) # 5+5+5+9
print(fourSumFast(L,40)) # 13+13+5+9
print(fourSumFast(L,62)) # 13+13+5+31
print(fourSumFast(L,98)) # 13+27+27+31
print(fourSumFast(L,0))
print(fourSumFast(L,10))
print(fourSumFast(L,29))
print(fourSumFast(L,89))