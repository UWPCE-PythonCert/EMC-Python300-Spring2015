import cPickle as pickle

class Foo(object):
    def __init__(self):
        print "init called"

foo = Foo()

foo_pickle = pickle.dumps(foo)

new_foo = pickle.loads(foo_pickle)

