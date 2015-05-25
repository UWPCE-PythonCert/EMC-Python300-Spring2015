
class Shape(object):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super(Shape, self).__init__(**kwargs)

class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super(ColoredShape, self).__init__(**kwargs)

if __name__ == '__main__':
    # variable argument definitions
    # why kwargs here
    # pitfall
    cs = ColoredShape(color='red', shapename='circle')
    assert cs.color == 'red'
