import sys
a = []
sys.getrefcount( a )
def test( x ): print "x has ref count = {}".format( sys.getrefcount( x ) )
test( a )
