class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        output = f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        return output

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height 

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**0.5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        line = ''
        for i in range(self.height):
            line += '*'*self.width+'\n'
        return line

    def get_amount_inside(self, other):
        area1 = self.width * self.height
        area2 = other.width * other.height
        amount = area1//area2
        return amount
    
class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        output = f'{self.__class__.__name__}(side={self.height})'
        return output

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)

rect = Rectangle(10,5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
sq.set_width(4)