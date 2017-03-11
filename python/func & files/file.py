
# Open a file
fo = open("adga.txt", "wb")  #enter file name "foo.txt"
print "Name of the file: ", fo.name       #print name of file
print "Closed or not : ", fo.closed        # tells file is opened or close by true|false
print "Opening mode : ", fo.mode              
fo.close()


print "Closed or not : ", fo.closed
