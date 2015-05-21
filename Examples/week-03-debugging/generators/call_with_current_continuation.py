import time
"""
this module is an example of building a generator
by chaining function callbacks
"""

def call_with_value(value):
    def inner(callback):
        time.sleep(3)
        print "callback {}".format(value)
        callback(value)
    return inner

def continuation_manager(wrapper):
    val = []
    def callback(*args, **kwargs):
        val[:] = [args, kwargs]

    wrapper(callback)
    return val


if __name__ == '__main__':
    # NOTE: execution
    # NOTE: return value
    for i in range(5):

        def wrapper( continuation_func ):
            call_with_value(i)( continuation_func )

        continuation_manager( wrapper )


