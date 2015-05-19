
class Parent( object ):

    def __init__(self, iterable):
        self.internal_state = []
        # which super gets called on override?
        self.update(iterable)

    def update(self, iterable):
        print "parent update"
        for i in iterable:
            self.internal_state.append(i)

    @property
    def data(self):
        return self.internal_state


class Child( Parent ):

    #  override
    def update(self,iterable):
        # 1. by super
        # 2. force super
        self.foobar = list(iterable)

if __name__ == '__main__':
    #
    #  based on Parent implementation
    #  we always expect self.internal_data to be
    #  created on intialization. 
    #  this is a condition that should be relied on
    #  while interfacing/subclassing the Parent
    #
    param_data = { 'a':1,'b':2,'c':3 }
    p = Parent( param_data )
    parent_state = p.data
    print "[ PARENT ]: {}".format(parent_state)
    assert parent_state == param_data.keys()

    #
    #  what happens if descendant overrides update?
    #
    c = Child( param_data )
    child_state = c.data
    print "[ CHILD ]: {}".format(child_state)
    assert child_state == param_data.keys()




    

