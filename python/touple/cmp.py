tuple1, tuple2 = (123, 'xyz'), (456, 'abc')

print cmp(tuple1, tuple2)
print cmp(tuple2, tuple1)
tuple3 = tuple2 + (786,);
print cmp(tuple2, tuple3)
