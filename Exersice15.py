height = (input("Enter all heights separated by a space: "))

#151 155 153 143 166

height_list = height.split(" ")
count = 0

for heights in height_list:
    count += 1

# print(height_list)

for i in range(count):
     height_list[i] = int(height_list[i])


total = 0

for person in height_list:
    total += person
average = total / count
# print(height_list)\
print("Avarage height is :",round(average))