class Hat:
    def __init__(self, **color_quant):
        contents = []
        for color, quant in color_quant.items():
            for i in range(quant):
                contents.append(color)
        self.contents = contents

hat1 = Hat(red=2, blue=1)