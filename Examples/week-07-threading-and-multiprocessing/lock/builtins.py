import threading
import time

def f(alist, adict, aint):
    alist[0] = aint
    adict['x'] = aint

if __name__ == '__main__':
    alist = [0]
    adict = { 'x': 0 }
    for n in range(1,1001):
        threading.Thread(target=f, args=(alist, adict, n)).start()

    print alist
    print adict


