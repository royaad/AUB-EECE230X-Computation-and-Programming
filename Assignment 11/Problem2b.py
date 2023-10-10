class Point():
    def __init__(self, x=0, y=0):
        # we can also use "Point" in str(type(Point(1,0.5))) for the assert
        assert (type(x)==int or type(x)==float) and (type(y)==int or type(y)==float), "Bad Input!"
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

class Rectangle():
    def __init__(self, p=Point(), q=Point()):
        assert isinstance(p, Point) and isinstance(q, Point) and p.x<=q.x and p.y<=q.y, "Bad Input!"
        self.p = p
        self.q = q
    def width(self):
        return self.q.x - self.p.x
    def height(self):
        return self.q.y - self.p.y
    def perimeter(self):
        return 2 * (self.width() + self.height())
    def area(self):
        return self.width() * self.height()
    def contains(self, other):
        assert isinstance(other, Point), "Bad Input!"
        return (self.p.x <= other.x <= self.q.x) and (self.p.y <= other.y <= self.q.y)
    def intersect(self, other):
        # additional function just for fun
        assert isinstance(other, Rectangle), "Bad Input!"
        return (other.p.x <= self.q.x and other.q.x >= self.q.x) and (other.p.y <= self.q.y and other.q.y >= self.p.y)
    def __str__(self):
        return '(p=' + str(self.p) + ',q=' + str(self.q) + ')'

R = Rectangle(Point(1,2),Point(3.2,4))
a = str(Point(1,2))
print(R)
print(R.width())
print(R.height())
print(R.area())
print(R.perimeter())
print(R.contains(Point(1.5,3)))
print(R.contains(Point(10.5,3)))