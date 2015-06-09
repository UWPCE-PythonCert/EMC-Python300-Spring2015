class ConfigAttr(object):

    def __init__(self,value):
        self._value = value

    def __get__(self, obj, obj_type=None):
        print "[ GET ]"
        return self._value

class MetaBase(type):

    def __new__(cls, name, bases, attrs):
        print "[ CLS ]: {}".format( cls )
        print "[ NAME ]: {}".format( name )
        print "[ BASES ]: {}".format( bases )
        print "[ ATTRS ]: {}".format( attrs )

        new_class = super(MetaBase, cls).__new__( cls, name, bases, attrs )

        fields = {}
        for obj_name, obj in attrs.items():
            if isinstance( obj, ConfigAttr ):
                fields[ obj_name ] = obj
                continue
            if obj_name.startswith( '__' ) and obj_name.endswith( '__' ):
                continue
        new_class.add_to_class( '_fields', fields )

        # required
        return new_class

    def add_to_class(cls, name, value):
        print "[ ADDING ]: {} = {}".format( name, value )
        setattr(cls, name, value)


class Base( object ):

    __metaclass__ = MetaBase

    def __init__( self, **kwargs ):
        print "[ KWARGS ]: {}".format( kwargs )

        for field_name, value in kwargs.items():
            print "[ FIELD ]: {} = {}".format(field_name, value)
            if self._fields.get( field_name, None ) is None:
                raise ValueError( 'class cannot set field attr where name = "%s" '
                    'field options are %s' % ( field_name, self._fields.keys() ) )
            setattr(self, field_name, value)
            kwargs.pop(field_name, None)


if __name__ == '__main__':
    pass

