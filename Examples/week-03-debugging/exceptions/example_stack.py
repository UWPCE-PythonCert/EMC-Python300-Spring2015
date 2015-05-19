
class StackBase( object ):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # what's this?
    def __repr__(self):
        return "{} {}".format(self.__class__,self.items)

    def __str__(self):
        return "{}".format(self.items)

class StackBack( StackBase ):
    """
    a stack built on the list type

    The 'top' of the stack is back of the list
    """

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class StackFront( StackBase ):
    """
    a stack built on the list type

    The 'top' of the stack is front of the list
    """
    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

if __name__ ==  '__main__':
    obj = "foo"

    s = StackBack()
    s.push(obj)
    assert s.pop() == obj

    s = StackFront()
    s.push(obj)
    assert s.pop() == obj

    s.push(obj)
    s.push(obj)
    while not s.is_empty():
        print s.pop() 


