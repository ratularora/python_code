import os, sys

# First go to the "/var/www/html" directory
os.chdir("/var/www/html" )

# Print current working directory
print "Current working dir : %s" % os.getcwd()

# Now open a directory "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# Use os.fchdir() method to change the dir
os.fchdir(fd)

# Print current working directory
print "Current working dir : %s" % os.getcwd()

# Close opened directory.
os.close( fd )