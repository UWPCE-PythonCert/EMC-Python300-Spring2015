
def log(self):
    print type(self)

A = type( 'A', (object,), { 'a_name' : 'A', 'log': log } )
B = type( 'B', (object,), { 'b_name' : 'B', 'log': log } )

MyClass = type( 'MyClass', (A,B,object), {} )

if __name__ == '__main__':
    a = A()
    print a.a_name
    print a.log()

    b = B()
    print b.b_name
    print b.log()

    c = MyClass()
    print c.a_name
    print c.b_name
    print c.log()

    

    
