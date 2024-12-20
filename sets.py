set1 = {10,56,89,90,"Jenny",True,10,1}
set2 = {}# that is dictionary
set3 = set() #that is set

#set1[2] = 99 can't change in set
set1.add(50)
set1.remove(10)
set1.discard(90)

set1.add((34,57,96))
# set1.add([45,55,34,456]) # cant add list
#set1.clear()
print(set1.pop())
print(set1)
#print(set1[0]) # that is can't to do

print(type(set1))
print(type(set2))
print(type(set3))
print(len(set1)) # // should show 10 items but this show 7 reson is duplicate elements