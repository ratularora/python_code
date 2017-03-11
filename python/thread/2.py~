import threading
import time

def loop1():
    for i in range(1, 11):
        time.sleep(1)
        print i

def loop2():
    for i in range(11, 21):
        time.sleep(1)
        print i

def loop3():
	while 1:
        	time.sleep(1)
        	print "hello"
threading.Thread(target=loop1).start()
threading.Thread(target=loop2).start()
threading.Thread(target=loop3).start()
