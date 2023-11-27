# Roy Aad

def pattern(k, mem={}):
    if k in mem: return mem[k]
    if k <= 1:
        mem[k] = "1"
        return "1"
    else:
        mem [k] = pattern(k - 1, mem) + "0" * k + pattern(k-2, mem)
        return mem[k]
    
for k in range(0,6):
    print("pattern("+str(k)+"): " + pattern(k))