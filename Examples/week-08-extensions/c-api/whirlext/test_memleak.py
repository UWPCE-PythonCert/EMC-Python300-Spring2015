from ext4 import *
import time, string
import mem_check

while True:
    #string_peek3(string.ascii_lowercase)
    string_peek4(string.ascii_lowercase)
    print "mem_use: %f MB" % mem_check.get_mem_use()
    
