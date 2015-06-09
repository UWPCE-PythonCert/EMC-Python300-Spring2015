# example from http://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/#Example-2:-Registering-Subclasses

class DBInterfaceMeta(type):

    # we use __init__ rather than __new__ here because we want
    # to modify attributes of the class *after* they have been
    # created
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            # this is the base class.  Create an empty registry
            cls.registry = {}
        else:
            # this is a derived class.  Add cls to the registry
            interface_id = name.lower()
            cls.registry[interface_id] = cls
            
        super(DBInterfaceMeta, cls).__init__(name, bases, dct)

class DBInterface(object):
    __metaclass__ = DBInterfaceMeta


class FirstInterface(DBInterface):
    pass

class SecondInterface(DBInterface):
    pass

class SecondInterfaceModified(SecondInterface):
    pass


if __name__ == '__main__':
    for k,v in DBInterface.registry.items():
        print k, v

    # NOTE: does this make sense?
    for k,v in SecondInterfaceModified.registry.items():
        print k, v


