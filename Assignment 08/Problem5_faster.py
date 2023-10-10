def distance(pt_1, pt_2):
    '''
    This function simply computes the L2 distance between 2 points pt_1 and pt_2
    '''
    return ((pt_1[0]-pt_2[0])**2 + (pt_1[1]-pt_2[1])**2)**0.5

def min_dist_nested(L, n):
    '''
    This function computes the distance using nested loops.
    It will be beneficial for small number of points.
    '''
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            tmp_dist = distance(L[i], L[j])
            if tmp_dist < min_dist:
                # print(L[i], L[j])
                min_dist = tmp_dist
    return min_dist

def min_dist_strip(midStrip, d):
    n = len(midStrip)
    for i in range(n):
        for j in range(i+1, n):
            if (midStrip[j][1] - midStrip[i][1]) < d:
                temp = distance(midStrip[i], midStrip[j])
                if temp < d:
                    d = temp
    return d

def min_dist_rec(Lx, Ly, n):

    assert n > 1, 'The array should contain at least 2 points'
    if n <= 3:
        return min_dist_nested(Lx, n)
    # Find the middle point along x
    mid = n//2
    # Divide points to the left and right of the mid.
    Lyl = []  # y sorted points on left of vertical line
    Lyr = []  # y sorted points on right of vertical line
    for i in range(n):
        if Ly[i][0] < Lx[mid][0] or (Ly[i][0] == Lx[mid][0] and Ly[i][1] < Lx[mid][1]):
            Lyl.append(Ly[i])
        else:
            Lyr.append(Ly[i])
    # Compute the smallest distance to the right and to the left
    dl = min_dist_rec(Lx[:mid], Lyl, mid)
    dr = min_dist_rec(Lx[mid:], Lyr, n-mid)
    # Find the smallest of the two
    d = min(dl, dr)
    # Check distances at the mid line
    midStrip = []
    for i in range(n):
        if -d < (Ly[i][0] - Lx[mid][0]) < d:
            midStrip.append(Ly[i])
            
    return min_dist_strip(midStrip, d)

def ClosestPairOfPoints(L):
    n = len(L)
    Lx = L.copy()                   # Copy L to Lx
    Ly = L.copy()                   # Copy L to Ly
    Lx.sort()                       # Sort Lx in non-decreasing order of x
    Ly.sort(key=lambda x:x[1])      # Sort Ly in non-decreasing order of y
    
    return min_dist_rec(Lx, Ly, n)

L = [(9, 1), (-9, -7), (3, -3), (-4, 6), (3, 3), (-8, 9), (-4, -6), (5, 8)]
print(ClosestPairOfPoints(L)) # Expected 5.0
L = [(6189, 6506), (1692, 7362), (7511, -5353), (-251, -1116), (-3247, -6400), (-6245, 7217), (807, 9479), (6873, -5442), (7592, -8114), (-3136, 1822), (5558, -7993), (-118, -8242), (9139, 9448), (-6647, -8413), (-2651, 1309), (2357, -4527), (202, 7992), (1918, 1760), (468, 4069), (4780, 102), (-1206, -8371), (-9387, 3070), (8431, 4849), (-6185, -7918), (-398, -8065), (-4495, -8848), (6417, 7736)]
print(ClosestPairOfPoints(L)) # Expected 331.25367922485026