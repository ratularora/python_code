# Open a file
fo = open("foo.txt", "r+")   #mention ur existing file 
str = fo.read(10);
print "Read String is : ", str
# Close opend file
fo.close()
