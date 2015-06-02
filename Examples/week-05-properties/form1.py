class Form1( object ):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print "GETTER"
        return self._name

    @name.setter
    def name(self,value):
        print "SETTER"
        self._name = value

    @name.deleter
    def name(self):
        print "DELETER"
        del self._name


