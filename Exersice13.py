import random

names = input("Enter names separatedby comma: ")
names = names.split(",")
# print(names)
# random_name = random.choice(names)
# print(f"hello {random_name},you have to pay the bill")

length = len(names)
random_choice = random.randint(0,length-1)
print(f"{names[random_choice]} will pay the bill")