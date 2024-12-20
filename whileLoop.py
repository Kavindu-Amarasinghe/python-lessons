# num_row = int(input("Enter the number of rows: "))
# for row in range(num_row+1):
#     for col in range(row):
#         print("*",end=" ")
#     print()

# count = 9

# while count > 0:print(count); count -= 1

# while count <= 10:
#      print(count)
#      count += 1
#      if count == 8:
#          break
# else:
#     print("Good Bye")
#
# number = int(input("Enter a number: "))
# while number != -1:
#     print(number)
#     number = int(input("Enter a number: "))
# else:
#     print("Thank you!")

total = 0
number = int(input("Enter a number(o to quit: "))

while number != 0:
    total += number
    number = int(input("Enter a number(o to quit: "))
print(f"total is {total}")
