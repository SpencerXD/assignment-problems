class Shape():
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color
    
    def describe(self):
        print('Base: ' + str(self.base))
        print('Height: ' + str(self.height))
        print('Color: ' + str(self.color))
        print('Perimeter: ' + str(self.perimeter))
        print('Area: ' + str(self.area))
        print('vertices: ' + str(self.vertices))

    def render(self, file_name):
        import matplotlib.pyplot as plt
        plt.style.use('bmh')

        plt.plot(
            [x[0] for x in self.vertices],
            [y[1] for y in self.vertices],
            color = self.color
        )
        plt.gca().set_aspect("equal")
        plt.savefig(file_name)
        plt.clf()


class Rectangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = 2*self.base + 2*self.height
        self.area = self.base*self.height
        self.vertices = [(0, 0), (self.base, 0), (self.base, self.height), (0, self.height), (0, 0)]
   
class RightTriangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = self.base + self.height + (self.base + self.height)**(1/2)
        self.area = (self.base/2)*self.height
        self.vertices = [(0, 0), (self.base, 0), (0, self.height), (0, 0)]
    

class Square(Shape):

    def __init__(self, base, color):
        super().__init__(base, base, color)
        self.perimeter = 2*self.base + 2*self.base
        self.area = self.base*self.base
        self.vertices = [(0, 0), (self.base, 0), (self.base, self.base), (0, self.base), (0, 0)]
       
print(">>> rect = Rectangle(5,2,'red)")
print('>>> rect.describe()')
rect = Rectangle(5,2,'red')

rect.describe()

rect.render('Rectangle.png')


print(">>> tri = RightTriangle(5,2,'blue')")
print('>>> tri.describe()')
tri = RightTriangle(5,2,'blue')

tri.describe()

tri.render('triangle.png')

sq = Square(5,'green')

sq.describe()

sq.render('Square.png')