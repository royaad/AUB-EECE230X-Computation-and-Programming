class ComplexNumber():
    def __init__(self, x=0, y=0):
        assert (type(x)==int or type(x)==float) and (type(y)==int or type(y)==float), "Bad Input!"
        self.x = x
        self.y = y
    def conj(self):
        return ComplexNumber(self.x, -self.y)
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** .5
    def inv(self):
        tmp = (self.x ** 2 + self.y ** 2)
        return ComplexNumber(self.x/tmp, -self.y/tmp)
    def __add__(self, other):
        real = self.x + other.x
        imag = self.y + other.y
        return ComplexNumber(real, imag)
    def __sub__(self, other):
        real = self.x - other.x
        imag = self.y - other.y
        return ComplexNumber(real, imag)
    def __mul__(self, other):
        real = self.x * other.x - self.y * other.y
        imag = self.x * other.y + self.y * other.x
        return ComplexNumber(real, imag)
    def __truediv__(self, other):
        tmp = (other.x ** 2 + other.y ** 2)
        real = (self.x * other.x + self.y * other.y)/tmp
        imag = (self.y * other.x - self.x * other.y)/tmp
        return ComplexNumber(real, imag)
    def __neg__(self):
        return ComplexNumber(-self.x, -self.y)
    def __str__(self):
        if self.y >= 0:
            return '(' + str(self.x) + '+' + str(self.y) + 'j)'
        else:
            return '(' + str(self.x) + str(self.y) + 'j)'

class Complex(ComplexNumber):
    def __init__(self, x=0, y=0):
        ComplexNumber.__init__(self, x, y)

# r = ComplexNumber(12)
# z = ComplexNumber(1.5, 2)
# t = Complex('a',1)
# print(r)
# print(z+t)
# print(-z)
# print(z*t)
# print(z*z.inv())
# print(z/t)
# print(z.conj())
# print(z.norm())