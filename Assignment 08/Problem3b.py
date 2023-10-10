def twoSumFast(L,t):
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
    
    L_copy = L.copy()
    L_copy.sort()
    return linearSorted2Sum(L_copy, t)



L = [-6, 1, 3, 5, 7, 8, 9, 11]
print(twoSumFast(L, 14)) # 7+7
print(twoSumFast(L, 12)) # 1+11 
print(twoSumFast(L, 15)) # 7+8
print(twoSumFast(L, 3))  # -6+3
print(twoSumFast(L, 0))  
print(twoSumFast(L, 7))
print(twoSumFast(L, 21))