class Circle :
    def __init__(self, radius=1):
        self.radius = radius
    def __str__(self):
        return f"radius = {self.radius}"

    def perimeter(self):
        return self.radius * 2 * 3.14

c1 = Circle(9)
print(c1.radius)
print(c1.perimeter())
print(c1)
c1.radius = 10
c1.corn = True

print(c1.perimeter())
print(c1.corn)

del c1.perimeter



