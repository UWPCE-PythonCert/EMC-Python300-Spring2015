
class Form2( object ):

    def __init__(self,name):
        self._name = name

    def get_name(self): 
        print "GETTER"
        return self._name

    def set_name(self,value):
        print "SETTER"
        self._name = value

    def del_name(self): 
        print "DELETER"
        del self._name

    name = property( get_name, set_name, del_name )

