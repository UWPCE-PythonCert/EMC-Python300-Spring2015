#!/usr/bin/env python

class NameMangler(type):

    def __new__(cls, clsname, bases, dct):

        new_attrs = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                new_attrs[name.upper()] = val
                new_attrs[name] = val
            else:
                new_attrs[name] = val

        return super(NameMangler, cls).__new__(cls, clsname, bases, new_attrs)

class Foo(object):
    __metaclass__ = NameMangler
    x = 1

if __name__ == "__main__":
    f = Foo()
    print f.x
    print f.X
