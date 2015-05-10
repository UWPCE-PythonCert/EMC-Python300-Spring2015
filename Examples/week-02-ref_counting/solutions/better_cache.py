import weakref
import sys
import gc

class PyObj(object):

    def __init__( self, pid ):
        self.pid = pid

class Cache( object ):

    def __init__( self ):
        self._store = weakref.WeakValueDictionary()

    def _find_or_create(self, obj):
        # NOTE: setdefault
        cached_obj = self._store.get(obj.pid, None)

        if cached_obj is None:
            self._store[ obj.pid ] = obj
            cached_obj = obj
       
        return cached_obj

    def find(self, obj):
        return self._find_or_create(obj)

    def get_ref_count(self):
        # NOTE: why is ref count so high?
        for key in self._store.keys():
            print "name={}, ref_count={}".format( key, sys.getrefcount( self._store[ key ] ) ) 

if __name__ == '__main__':
    cache = Cache()

    foo = cache.find( PyObj( 'foo' ) )
    assert foo.pid == 'foo'
    print "[ FOO ]: {}".format( sys.getrefcount( foo ) )
    del foo

    bar = cache.find( PyObj( 'bar' ) )
    assert bar.pid == 'bar'  
    print "[ BAR ]: {}".format( sys.getrefcount( bar ) )
    del bar
    
    baz = cache.find( PyObj( 'baz' ) )
    assert baz.pid == 'baz'  
    print "[ BAZ ]: {}".format( sys.getrefcount( baz ) )
    del baz

    print gc.collect()
    cache.get_ref_count()
    





