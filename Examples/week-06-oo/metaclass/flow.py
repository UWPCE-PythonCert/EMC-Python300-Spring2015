class FlowMeta(type):
    
    def __new__(cls, name, bases, attrs):
        print "__new__ metaclass"
        return super( FlowMeta, cls ).__new__( cls, name, bases, attrs )

    def __init__(cls, name, bases, attrs):
        print "__init__ metaclass"


class Flow(object):

    __metaclass__ = FlowMeta

    def __new__(cls, *args, **kwargs):
        print "__new__"
        return super( Flow, cls ).__new__( cls, *args, **kwargs )

    def __init__(self, *args, **kwargs):
        print "__init__"

if __name__ == '__main__':
    f = Flow()


    
