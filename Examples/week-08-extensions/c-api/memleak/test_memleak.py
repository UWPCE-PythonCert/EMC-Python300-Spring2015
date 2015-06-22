from memleak import memleak
import time
import mem_check

while True:
    memleak()
    print "mem_use: %f MB" % mem_check.get_mem_use()
    
