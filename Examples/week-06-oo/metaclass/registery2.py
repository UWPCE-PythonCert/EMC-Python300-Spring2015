# example from http://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/#Example-2:-Registering-Subclasses

class DBInterfaceMeta(type):
    pass

class DBInterface(object):
    __metaclass__ = DBInterfaceMeta


class FirstInterface(DBInterface):
    pass

class SecondInterface(DBInterface):
    pass

class SecondInterfaceModified(SecondInterface):
    pass


def recurse_subs(level_list):
    for sub in level_list:
        next_level = [ next_sub for next_sub in sub.__subclasses__() if issubclass( next_sub, DBInterface ) ]
        print sub
        if next_level:
            recurse_subs( next_level )

if __name__ == '__main__':

    recurse_subs( DBInterface.__subclasses__() )
        
