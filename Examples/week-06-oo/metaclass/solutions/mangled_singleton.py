#!/usr/bin/env python

class NameMangler(type):

    def __new__(cls, clsname, bases, dct):
        new_attrs = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                new_attrs[name.upper()] = val
                new_attrs[name] = val
                new_attrs[name.upper()+name.upper()] = val
                new_attrs[name+name] = val
            else:
                new_attrs[name] = val

        return super(NameMangler, cls).__new__(cls, clsname, bases, new_attrs)

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

class MangledSingleton( Singleton, NameMangler ):
    pass

class MyClass(object):
    __metaclass__ = MangledSingleton
    x = 1

if __name__ == '__main__':

    # does it pass the Singleton test?
    object1 = MyClass()
    object2 = MyClass()
    assert id(object1) == id(object2)

    # does it pass the mangling test?
    print "[ x ]: ", object1.x
    assert object1.x == 1
    print "[ X ]: ", object1.X
    assert object1.X == 1
    print "[ xx ]: ", object1.xx
    assert object1.xx == 1
    print "[ XX ]: ", object1.XX
    assert object1.XX == 1

    


