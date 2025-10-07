import random

class Hat:
    def __init__(self, **color_quant):
        contents = []
        for color, quant in color_quant.items():
            for i in range(quant):
                contents.append(color)
        self.contents = contents
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.contents})'
    
    def draw(self, number):
        if number > len(self.contents):
            all = self.contents.copy()
            self.contents = []
            return all
        else:
            drawback = random.sample(self.contents, number)
            for i in drawback:
                self.contents.remove(i)
            return drawback             


hat1 = Hat(red=2, blue=1)
print(hat1)
print(hat1.draw(2))
