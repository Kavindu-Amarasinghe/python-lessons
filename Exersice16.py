numbers = input("Enter all numbers you want and separate by ' ': ")
number_list = numbers.split(' ')
count = 0

for x in number_list:
    count = count + 1

for i in range(count):
    number_list[i] = int(number_list[i])

maximum_number = number_list[0]

for number in number_list:
    if number > maximum_number:
        maximum_number = number


print(maximum_number)



# print(number_list)