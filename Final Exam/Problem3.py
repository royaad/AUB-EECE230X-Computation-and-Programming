# Roy Aad

def pattern(k):
    if k <= 1:
        return "1"
    else:
        return pattern(k - 1) + "0" * k + pattern(k-2)
    
for k in range(0,6):
    print("pattern("+str(k)+"): " + pattern(k))