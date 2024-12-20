# a = 52
# if a%2 == 0:
#     print("Even")
#     if (a>30):
#         print("Number is greater than 30")
# print("Bye")

height = int(input("Enter height in inches: "))

if height > 3:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Please Pay 150 Rs")
    elif age <= 18:
        print("Please Pay 250 Rs")
    else:
        print("Please Pay 500 Rs")
else:
    print("can't ride")
print("Bye")