class Name(object):
    def __init__(self,val):
        self.value = val

    def __get__(self, obj, objtype):
        print 'GETTER'
        return self.value

    def __set__(self, obj, val):
        print 'SETTER'
        self.value = val

    def __delete__(self,obj):
        print 'DELETER'
        del self.value

class Form3(object):

    def __init__( self, name ):
        self.__class__.name = Name( name )
        self.__dict__['name'] = 'BOOM!'

    
