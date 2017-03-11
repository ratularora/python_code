import os

# Open a file
path = "/home/ratul"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file
