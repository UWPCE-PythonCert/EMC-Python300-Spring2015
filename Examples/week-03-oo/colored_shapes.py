
class Shape(object):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super(Shape, self).__init__(**kwargs)

class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        print color
        print kwargs
        self.color = color
        super(ColoredShape, self).__init__(**kwargs)

if __name__ == '__main__':
    cs = ColoredShape(color='red', shapename='circle')
    assert cs.color == 'red'
