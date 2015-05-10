
class PyObjWithDel(object):

    def __del__(self):
        print "deleting %s object at %s" % (self.__class__.__name__, id(self))


class PyObjNoDel(object):
    pass


if __name__ == '__main__':
    
    #
    #  use __del__ only to show
    #  that reference counting handles
    #  things immediately. But in general
    #  never use __del__, ever
    #
    print "[ EXAMPLE 1 ]"
    x = PyObjWithDel()
    x = None
    x = PyObjWithDel()
    del x

    #
    # show where GC with circular refs comes in
    #
    print "[ EXAMPLE 2 ]"
    import gc
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_OBJECTS)
    x = PyObjNoDel(); y = PyObjNoDel();
    x.other = y; y.other = x
    # ref counting will not handle these cycles
    x = None
    y = None
    print gc.collect()
    print gc.garbage

    #
    #  GC does not work with __del__
    #
    print "[ EXAMPLE 3 ]"
    import gc
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_OBJECTS)
    x = PyObjNoDel(); y = PyObjWithDel();
    x.other = y; y.other = x
    # ref counting will not handle these cycles
    x = None
    y = None
    # oops, neither will GC
    print gc.collect()
    print gc.garbage


    
    





