
def my_method(self):
    print "called my_method, x = %s" % self.x

MyClass = type('MyClass',(object,), {'x': 1, 'my_method': my_method})

if __name__ == '__main__':
    instance = MyClass()
    print instance.my_method()
    print instance.x

