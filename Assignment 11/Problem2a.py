class Point():
    def __init__(self, x=0, y=0):
        # we can also use "Point" in str(type(Point(1,0.5))) for the assert
        assert (type(x)==int or type(x)==float) and (type(y)==int or type(y)==float), "Bad Input!"
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

class Circle():
    def __init__(self, center=Point(), radius=1):
        assert isinstance(center, Point), "Bad Input!"
        assert (type(radius)==int or type(radius)==float) and (radius>=0), "Bad Input!"
        self.center = center
        self.radius = radius
    def diameter(self):
        return 2 * self.radius
    def perimeter(self):
        from math import pi
        return 2 * pi * self.radius
    def area(self):
        from math import pi
        return pi * self.radius ** 2
    def contains(self, other):
        assert isinstance(other, Point), "Bad Input!"
        l2_dist = (other.x - self.center.x)**2 + (other.y - self.center.y)**2
        return l2_dist <= self.radius**2
    def intersect(self, other):
        assert isinstance(other, Circle), "Bad Input!"
        l2_dist = (other.center.x - self.center.x)**2 + (other.center.y - self.center.y)**2
        return l2_dist <= (self.radius + other.radius)**2
    def __str__(self):
        return '((' + str(self.center.x) + ',' + str(self.center.y) + '),' + str(self.radius) + ')'

C1 = Circle()
C2 = Circle(Point(1,0.5),0.75)
C3 = Circle(Point(10,5),2)
print(C1)
print(C2)
print(C3)
print(C1.diameter())
print(C2.perimeter())
print(C3.area())
print(C1.contains(Point(0.5,0.5)))
print(C1.contains(Point(5,5)))
print(C1.intersect(C2))
print(C1.intersect(C3))