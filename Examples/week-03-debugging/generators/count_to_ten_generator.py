def count_to_10():
    print "executing..."
    for i in range(10):
        j = yield i
        print "continue..." 
        #print "received {}".format(j)

if __name__ == '__main__':
    # NOTE: sequence of events
    # NOTE: adheres to iterator protocol
    print list(count_to_10())
