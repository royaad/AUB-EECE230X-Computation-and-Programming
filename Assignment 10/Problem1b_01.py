def genBinStr2(n, w, tmp={}):
    # check if the result is already memoized
    if (n, w) in tmp: return tmp[(n, w)]
    if n < 0 or w < 0 or w > n: return []
    if n == 0 and w == 0: return ['']
    if n == 1:
        if w == 0: return ["0"]
        if w == 1: return ["1"]
        
    X = genBinStr2(n - 1, w, tmp)
    Y = genBinStr2(n - 1, w - 1, tmp)
    Z = []

    if w < n:
        for s in X:
            Z.append("0" + s)
    if w >= 1:
        for m in Y:
            Z.append("1" + m)

    # memoize the result in a temporary dictionary before returning it
    tmp[(n, w)] = Z
    return Z

print(genBinStr2(4, 2))