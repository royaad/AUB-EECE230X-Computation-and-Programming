def searchHybrid(L,x): # Wrapper function
    '''
    Assumes L is a list sorted in nondecreasing order
    returns index of an occurence of x in L if found
    else returns -1
    Algorithm: hybrid binary-search linear-search
    '''

    def linearSearch(L, x, low, high):
        '''Assumes L is a list sorted in nondecreasing order
        returns index of an occurence of x in L[low...high] if found
        else returns -1
        Algorithm: linear-search
        '''
        for i in range(low, high+1): 
            if L[i]==x:
                return i
        return -1

    def recBinarySearchHybrid(L, x, low, high):
        '''
        Assumes L is a list sorted in nondecreasing order.
        returns index of an occurence of x in L[low...high] if found, else returns -1.
        Algorithm: hybrid binary-search linear-search: use linear search if size of L[low...high]
        is at most 5.
        '''
        if low>high: return -1 # base case 1
        if high-low < 5: return linearSearch(L, x, low, high)
        mid = (low+high)//2
        if L[mid] == x: 
            return mid # base case 2 
        elif L[mid]<x:
            return recBinarySearchHybrid(L,x,mid+1, high)
        else: 
            return recBinarySearchHybrid(L,x,low, mid-1)

    return recBinarySearchHybrid(L,x,0,len(L)-1)


print("searchHybrid([],3):",searchHybrid([], 3))
print("searchHybrid([5],3):",searchHybrid([5], 3))
print("searchHybrid([5], 5):",searchHybrid([5], 5))
L = [2*i for i in range(21)] # L = [0,2,....,40]
print("L=",L)
print("searchHybrid(L, i) for i =-1,..., 41:")
for i in range(-1,42):
    print(searchHybrid(L, i),end=" ")