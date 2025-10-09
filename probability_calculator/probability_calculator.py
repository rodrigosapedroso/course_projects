import copy
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
        drawback = random.sample(self.contents, number)
        for i in drawback:
            self.contents.remove(i)
        return drawback          


hat1 = Hat(black=6, red=4, green=3)
print(hat1)
print(hat1.draw(5))

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    N = num_experiments
    M = 0
    
    for i in range(N):
        cases = []
        hat_copy = copy.deepcopy(hat)
        l_drawn = hat_copy.draw(num_balls_drawn)
        for color, quant in expected_balls.items():
            if l_drawn.count(color) >= quant:
                cases.append('yes')
            else:
                cases.append('no')
        if all(i == 'yes' for i in cases):
            M += 1
    
    prob = M/N
    return prob

probability = experiment(hat1, {'red':2,'green':1}, 5, 2000)
print(probability)