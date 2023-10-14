def partition2(A,p,r):
    x = A[r]
    i1 = p-1
    i2 = p-1
    for j in range(p,r):
        if A[j]==x:
            i2+=1
            (A[i2],A[j])=(A[j],A[i2])
        elif A[j]<x:
            i1+=1
            i2+=1
            if i2==j:
                (A[i1],A[i2])=(A[i2],A[i1])
            elif i1==i2:
                (A[i1],A[j])=(A[j],A[i1])
            else:
                (A[i2],A[i1],A[j])=(A[i1],A[j],A[i2]) 
    i2+=1
    i1+=1
    (A[i2],A[r])=(A[r],A[i2])
    return (i1,i2)

import numpy.random as rand

def randPartition2(A,p,r):
    randIndex = rand.randint(p,r+1)  
    # generate random number between p and r inclusive 
    (A[randIndex],A[r])=(A[r],A[randIndex])  
    # Exchange A[randIndex] with A[r]
    return partition2(A,p,r)

def randQuickSort2(A): # Wrapper function 
    def randQuickSortRec(A,p,r):
        print(p,r)
        if p<r: 
            q1, q2 = randPartition2(A,p,r)
            randQuickSortRec(A,p,q1-1)
            randQuickSortRec(A,q2+1,r) 
    randQuickSortRec(A,0,len(A)-1)
    
## The code below creates a Stack class and uses the same approach of the recursive function above only using a while loop
class Stack(list):
    """ class Stack derived from list"""
    def push(self,value):
        self.append(value)
    def top(self):
        assert not self.isEmpty(), "Stack Empty!"
        return self[len(self)-1]
    def isEmpty(self):
        return (len(self)==0)

def randQuickSortIterative(A):
    S = Stack()
    S.push([0, len(A)-1])
    while not S.isEmpty():
        p, r = S.pop()
        # print(p, r)
        if p<r:
            q1, q2 = randPartition2(A,p,r)
            if q2+1<r: # not necessary we can simply push. Then the verification will be done during the pop
                S.push([q2+1,r])
            if p<q1-1: # not necessary we can simply push. However, it seems to increase the time a bit.
                S.push([p,q1-1])
    
A1=[]
A2=[1]
A3=[0,1,2,0,1,2,0,1,2,1]
A4=[5,6,5,5,1,3,5,2,1,7,9,5,15,100,5, 2,17,5,56]

for A in (A1,A2,A3,A4):
    randQuickSortIterative(A)
    print("A sorted:",A)

C = [18, -18, -8, -14, 16, 10, -7, -18, 4, 15, 0, -13, 14, -20, -10, 5, -1, 17, 11, -7, -5, 3, -1, 4, -16, -12, 14, -4, -12, 15, -3, -11, 18, 11, 12, -18, 18, 9, -5, 9, -5, 5, -20, 14, 12, -1, -18, 13, 0, 4, 20, 0, -1, -15, 17, -12, -19, 5, 13, 1, 20, 1, 2, 3, -6, -1, -16, -18, 1, -20, 5, -5, -13, -13, -8, 12, -7, -18, -17, -7, -13, 20, -6, 8, -1, -1, 7, 4, -18, 4, 9]
# estimating the average time for sorting
import timeit
elapsed_time = []
for n in range(10000):
    start_time = timeit.default_timer()
    randQuickSortIterative(C)
    end_time = timeit.default_timer()
    elapsed_time.append(end_time - start_time)

print(f"Time taken: {sum(elapsed_time)/len(elapsed_time)} seconds")
print(C)