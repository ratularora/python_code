import time;

localtime = time.asctime( time.localtime(time.time()) )
print time.time()
print time.localtime(time.time())
print "Local current time :", localtime
