def genBinStr2(n,w):
    if n < 0 or w < 0 or w > n: return [] # inacceptable cases, return empty list
    if n == 0 and w == 0: return [''] # base case 0: n=0, w=0 -> ['']
    if n == 1:
        if w == 0: return["0"] # base case 1: n=1, w=0 -> ['0']
        if w == 1: return["1"] # base case 2: n=1, w=1 -> ['1']
    X = genBinStr2(n-1,w)      # will contain the cases with n-1 zeros and w ones. i.e. n=3, w=1 -> ["01", "10"]
    Y = genBinStr2(n-1,w-1)    # will contain the cases with n-1 zeros and w-1 ones. i.e. n=3, w=1 -> ["00"]
    Z = []
    if w < n:
        for s in X:
            Z.append("0"+s) # add zero to the start of ["01", "10"] -> ["001", "010"]
    if w >=1:
        for m in Y:
            Z.append("1"+m) # add one to the start of ["00"] -> ["100"]
    return Z

print(genBinStr2(4, 2))