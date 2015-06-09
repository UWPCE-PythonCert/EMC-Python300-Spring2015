class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None 

    def __call__(cls,*args,**kw):
        #
        #  this runs the first 
        #  time MyClass() constructor is invoked
        #  it is called before the MyClass
        #  __new__ and __init__
        #
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance

class MyClass(object):
    __metaclass__ = Singleton


if __name__ == '__main__':
    object1 = MyClass()
    object2 = MyClass()
    print id(object1)
    print id(object2)

# NOTE: init, new, call
