numbers=[10,0,-1,7,12,33,44,323,4454]
names=["Kamal","Nimal","Sunil"]
mix_list=[1,"Kamal","Nimal",10.10,True]
print(numbers)
print(names)
print(mix_list)
print(len(numbers))
print(names[-1])

print(numbers[0:9:2])
print(numbers.sort())
print(max(numbers))
print(min(numbers))
print(mix_list)
numbers.append(45)
print(numbers)
numbers.insert(2,8768)
print(numbers)
numbers.extend([45,46,47,48,49])
print(numbers)
numbers.remove(49)
print(numbers)
# numbers.pop()
print(numbers.pop())
