def tileDefectiveChessBoard(n,i,j): # Wrapper function
    """ Tile an n by n tileDefective chess board with missing cell (i,j)
    Function assumes n is a power of 2, 0<=i<=n-1,and 0<=j<=n-1 """
    def tileDefectiveChessBoardRec(A, tileIndex, startX, endX, startY, endY, i, j):
        """Tile defective chess board [startX ... endX]*[startY ... endY] with missing cell (i,j)
        Function assumes that endX-startX+1 = endY-startY+1 is a power of 2
        It also assumes that startX <=i<=endX and startY <=j<=endY """
        n = endX-startX+1
        if n == 1: # if n equals 1, do nothing.
            return
        elif n == 2: # if n equals 2, fill all cells except cell (i,j) with tileIndex 
            for k in range(startX, endX+1):
                for l in range(startY, endY+1):
                    if k!=i or l!=j:
                        A[k][l] = tileIndex
            return tileIndex + 1
        else: # if n > 2, split the board into 4 quadrants.
            nX = (endX+startX+1)//2 # nX indicates the X middle index.
            nY = (endY+startY+1)//2 # nY indicates the Y middle index.
            # check the position of the defect
            if i < nX and j < nY:
                A[nX][nY-1]=A[nX][nY]=A[nX-1][nY]=tileIndex # fill the cells in the quadrants that have no defects
                tileIndex+=1 # increment the tile once filled
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, startY, nY-1, i, j) # recursive call on the 1st quadrant
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, nY, endY, nX-1, nY) # recursive call on the 2nd quadrant
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, startY, nY-1, nX, nY-1) # recursice call on the 3rd quadrant
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, nY, endY, nX, nY)       # recursive call on the 4th quadrant
                return tileIndex
                # we can define the start, end, and defect position for each quadrant and do the recursive calls outside the ifs
            if i < nX and j >= nY:
                A[nX-1][nY-1]=A[nX][nY-1]=A[nX][nY]=tileIndex
                tileIndex+=1
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, startY, nY-1, nX-1, nY-1)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, nY, endY, i, j)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, startY, nY-1, nX, nY-1)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, nY, endY, nX, nY)
                return tileIndex
            if i >= nX and j < nY:
                A[nX-1][nY-1]=A[nX-1][nY]=A[nX][nY]=tileIndex
                tileIndex+=1
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, startY, nY-1, nX-1, nY-1)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, nY, endY, nX-1, nY)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, startY, nY-1, i, j)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, nY, endY, nX, nY)
                return tileIndex
            if i >= nX and j >= nY:
                A[nX-1][nY-1]=A[nX-1][nY]=A[nX][nY-1]=tileIndex
                tileIndex+=1
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, startY, nY-1, nX-1, nY-1)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, startX, nX-1, nY, endY, nX-1, nY)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, startY, nY-1, nX, nY-1)
                tileIndex = tileDefectiveChessBoardRec(A, tileIndex, nX, endX, nY, endY, i, j)
                return tileIndex

    ## first call of the wrapper function
    A = [[None for v in range(n)] for u in range(n)]
    A[i][j] = 0 # zero indicates the missng cell
    tileDefectiveChessBoardRec(A, 1, 0, n-1, 0, n-1, i, j) #set the parameter tileIndex to 1
    return A

# Test program
import numpy # numerical python module
for (n,i,j) in ((1,0,0),(2,0,0),(2,0,1),(2,1,1),(4,0,0),(8,0,0),(8,2,4),(16,3,5)):
    print("\ntileDefectiveChessBoard("+str(n)+","+str(i)+","+str(j)+")")
    A = tileDefectiveChessBoard(n,i,j)
    print(numpy.matrix(A))