def multMatrices(A,B):
    """ A and B are lists of lists representing two 2 by 2 matrices"""
    C00 = A[0][0]*B[0][0]+A[0][1]*B[1][0]
    C01 = A[0][0]*B[0][1]+A[0][1]*B[1][1]
    C10 = A[1][0]*B[0][0]+A[1][1]*B[1][0]
    C11 = A[1][0]*B[0][1]+A[1][1]*B[1][1]
    C = [[C00, C01], [C10, C11]]
    return C

def fibMatrixVersion(n): #Wrapper function
    """ Assumes n is a non-negative integer """
    # This is based on the previous power problem.
    def recMatrixPowerFast(X,n):
        """ X is a list of lists representing a 2 by 2 matrix and n is non-negative integer"""
        if n == 1:
            return X
        if n%2:
            temp = recMatrixPowerFast(X, n-1)
            return multMatrices(temp, X)
        if n==2:
            return multMatrices(X, X)
        temp = recMatrixPowerFast(X, n//2)
        return multMatrices(temp, temp)
    if n == 0:
        return 0
    A = [[1, 1], [1, 0]]
    C = recMatrixPowerFast(A,n)
    return C[0][1]


for i in range(11):
    print("F_",i,":", fibMatrixVersion(i))
print("F_ 100 :", fibMatrixVersion(100))