
class A( object ):

    def __init__(self):
        self.a_name = 'A'

    def log(self):
        print self.__class__.__name__


class B( object ):

    def __init__(self):
        self.b_name = 'B'

    def log(self):
        print self.__class__.__name__


# Exercises:
# 1. can you create these classes using 'type' syntax
# 2. create a third class 'MyClass' that inherits from A and B using 'type' syntax

