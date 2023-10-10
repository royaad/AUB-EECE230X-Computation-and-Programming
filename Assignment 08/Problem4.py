def  merge(L, R): # Time: O(len(L)+len(R))
    """ Assumes L (left) and R (right) are lists of numbers sorted in non-decreasing order
        Returns a list C consisting L and R merged in non-decreasing order """
    C = []     ## initialize C to the empty list
    m = len(L)
    n = len(R)
    i = 0 # counter to traverse L 
    j = 0 # counter to traverse R
    while i!=m and j !=n: 
        if L[i]<R[j]: 
            C.append(L[i])
            i+=1
        else: 
            C.append(R[j])
            j+=1
    while i!=m: # if R is done, append remaining elements of L to C 
        C.append(L[i])
        i+=1       
    while j!=n: # if L is done, append remaining elements of R to C 
        C.append(R[j])
        j+=1      
    return C

def ternaryMergeSort(A, low, high): 
    # Base case: if low==high, in which case nothing to be done: 
    #  as a size-1    list is already sorted
    if low<high:
        third = low + (high - low)//3
        twoThird = low + 2*(high - low)//3
        ternaryMergeSort(A, low, third)         # first recursive call 
        ternaryMergeSort(A, third+1, twoThird)  # second recursive call
        ternaryMergeSort(A, twoThird+1, high)   # third recursive call
        temp = merge(A[low:third+1], A[third+1:twoThird+1])
        A[low:high+1] = merge(temp, A[twoThird+1:high+1])
        # Recall that A[a:b+1] gives  A[a ... b]

A = [5,6,1,3,2,1,7,9,5,15,100, 2,17,56]
ternaryMergeSort(A, 0, len(A)-1)
print(A)
A = [2,1]
ternaryMergeSort(A, 0, len(A)-1)
print(A)
A = []
ternaryMergeSort(A, 0, len(A)-1)
print(A)
A= [1]
ternaryMergeSort(A, 0, len(A)-1)
print(A)
A = [20-i for i in range(20)] #, i.e., [20,19, ..., 1]
ternaryMergeSort(A, 0, len(A)-1)
print(A)

''' the running time of Ternary Merge Sort.
T(n) = 3*T(n/3) + c*n       if n = 3, 9, 27...
T(n) = c0                   if n = 1

according to Master Theorem
a = 3
b = 3
k = 1
logb(a) = 1 = k
then T(n) = Θ(n*log(n))
'''

import time
start_time = time.time()
C = [18, -18, -8, -14, 16, 10, -7, -18, 4, 15, 0, -13, 14, -20, -10, 5, -1, 17, 11, -7, -5, 3, -1, 4, -16, -12, 14, -4, -12, 15, -3, -11, 18, 11, 12, -18, 18, 9, -5, 9, -5, 5, -20, 14, 12, -1, -18, 13, 0, 4, 20, 0, -1, -15, 17, -12, -19, 5, 13, 1, 20, 1, 2, 3, -6, -1, -16, -18, 1, -20, 5, -5, -13, -13, -8, 12, -7, -18, -17, -7, -13, 20, -6, 8, -1, -1, 7, 4, -18, 4, 9]
print(ternaryMergeSort(C , 0 , len(C)-1))
# A = [20-i for i in range(20)]
# print(ternaryMergeSort(A , 0 , len(A)-1))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")