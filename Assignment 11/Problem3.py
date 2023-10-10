class Vector(list):
    def __init__(self, other):
        assert len(other)!=0, "Invalid Input!"
        for e in other:
            assert type(e)==int or type(e)==float, "Invalid Input!"
        list.__init__(self, other)
    def __add__(self, other):
        assert len(self)==len(other), "Invalid Input!"
        tmp = []
        for i in range(len(self)):
            tmp.append(self[i]+other[i])
        return Vector(tmp)
    def __sub__(self, other):
        assert len(self)==len(other), "Invalid Input!"
        tmp = []
        for i in range(len(self)):
            tmp.append(self[i]-other[i])
        return Vector(tmp)
        # since neg is defined, we can use one line of code -> return self + (-other)
        # however, this is less efficient since it does 2 iterations instead of one.    
    def __mul__(self, other):
        assert len(self)==len(other), "Invalid Input!"
        tmp = 0
        for i in range(len(self)):
            tmp += self[i]*other[i]
        return tmp
    def __neg__(self):
        tmp = []
        for i in range(len(self)):
            tmp.append(-self[i])
        return Vector(tmp)
    def norm(self):
        return (self*self)**.5
    def __str__(self):
        out_str = '<'
        for e in self:
            out_str += str(e) + ','
        return out_str[:-1] + '>'

def zeros(n):
    assert n>0, "Invalid Input!"
    return Vector([0]*n)

def ones(n):
    assert n>0, "Invalid Input!"
    return Vector([1]*n)

v = Vector([1,2.3])
w = zeros(5)
u = ones(2)
print(v)
print(w)
print(v[1])
print(v+v+v)
print(v*u)
print(v.norm())
w[2]=3.5
import copy
v = copy.deepcopy(w)
print(v)
print(-v)
w[0] = 15.5
w[4] = -12
print(w-v)
print(-w+v)