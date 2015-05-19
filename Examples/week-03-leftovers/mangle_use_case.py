
class Parent( object ):

    def __init__(self, iterable):
        self.internal_state = []
        self.__update(iterable)

    def update(self, iterable):
        print "Parent.update() called"
        for i in iterable:
            self.internal_state.append(i)
    __update = update

    @property
    def data(self):
        return self.internal_state


class Child( Parent ):

    #  override
    def update(self,iterable):
        # 1. super call works?
        print "Child.update() called"
        self.foobar = list(iterable)

if __name__ == '__main__':
    #
    #  based on Parent implementation
    #  we always expect self.internal_data to be
    #  created on intialization and consistent
    #
    param_data = { 'a':1,'b':2,'c':3 }
    p = Parent( param_data )
    parent_state = p.data
    print "[ PARENT ]: {}".format(parent_state)
    assert parent_state == param_data.keys()

    #
    #  what happens if descendant overries update?
    #
    c = Child( param_data )
    child_state = c.data
    print "[ CHILD ]: {}".format(child_state)
    assert child_state == param_data.keys()




    

