tuple1 = (12,66,-8,"jenny",True)
tuple2=(45,) # that is not tuple
tuple3= (45,) # that is tuple
tuple4=(tuple1,tuple3) # nesting tuple
tuple5=(45,67,90)

list1=[1,2,3,4,5,6,7,8,9,10]

tuple6=(10,)*5

# tuple1[0] = 13 # --- tuple mehema rewrite karanna ba



print(tuple1[1])
print(tuple1[-2])
print(type(tuple2))
print(type(tuple3))

print(tuple1[1:4])
print(tuple1[::])

print(len(tuple1))

print(tuple4[0])
print(len(tuple4))
print(min(tuple5))
print(tuple5.count(67))
print(tuple5.index(67))
print(tuple(list1)) # list -----> tuple
print(tuple6)