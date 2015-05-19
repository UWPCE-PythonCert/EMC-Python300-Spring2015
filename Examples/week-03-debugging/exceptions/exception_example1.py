def divide(x, y):
    try:
        print "line 1"
        result = x / y
        print "line 2"

    except ZeroDivisionError as e:
        print "caught division error: %s" % str(e)

    except Exception as e:
        print "unhandled exception %s.  message: %s " % (type(e), e.args)
        raise

    else:
        print "everything worked great"
        return result

    finally:
        print "this is executed no matter what"

divide(2,0)
