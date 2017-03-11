import os, sys

# listing directories
print "The dir is: %s" %os.listdir(os.getcwd())  #getcwd redirect to home path

# removing
os.remove("aa.txt")  # delete the file

# listing directories after removing path
#print "The dir after removal of path : %s" %os.listdir(os.getcwd())
