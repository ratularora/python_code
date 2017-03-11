list1, list2 = ['xyz'], ['abc']
list4 = ['xyz',0,0]
print cmp(list1,list4)
print cmp(list1, list2)
print cmp(list2, list1)
list3 = list2 + [786];
print list3
print cmp(list4,list3)
print cmp(list2, list3)
