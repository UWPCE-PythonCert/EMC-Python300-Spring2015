class ParentFoo(object):
    def bound_method(self):
        print "ParentFoo bound_method"

    @classmethod
    def unbound_method(cls):
        print "ParentFoo unbound_method"

class FooChild(ParentFoo):

    def bound_method(self):
        print "FooChild bound_method"

    @classmethod
    def unbound_method(cls):
        print "FooChild unbound_method"

if __name__ == '__main__':
    foo = FooChild()
    foo.bound_method() # method is bound to the foo instance
    FooChild.unbound_method() # method is not bound
