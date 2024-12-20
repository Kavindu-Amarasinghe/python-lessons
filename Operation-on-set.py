set1 = {'Ram','Shyam','Jenny'}
set2 = {'Jenny','Jiya','Aakash'}
set3 = {'Ankur','Pradeep'}

# print(set1.union(set2,set3))
# print(set2.union(set1))
#
# print(set1 | set2) # same output
#
# print(set1 & set2)
#
# print(set1.union(('Mohan','Jenny')))
# # print(set1 | ('Mohan','Jenny')) that is error point
#
# set1.update(set2)
# print(set1)
#
# set1.update(['Mohan','jenny'])
# print(set1)

#set1 |= set2
#print(set1)

# print(set1.intersection(set2))

# print(set1.difference(set2))

# print(set1.symmetric_difference(set2))

# print(set1 ^ set2 ^ set3)
#
# set2.symmetric_difference_update(set1)

print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
print(set1<=set1)