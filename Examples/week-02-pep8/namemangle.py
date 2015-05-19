

class Foo( object ):

    def _foo(self):
        print "foo"

    def __bar(self):
        print "bar"

class Baz( Foo ):

    def __bar(self):
        print "BazBar"

