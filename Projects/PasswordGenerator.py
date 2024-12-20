import random

print("Welcome to Password Generator")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','(',')','*','+']

n_letters = int(input("How many letters you want in your password? \n"))
n_numbers = int(input("How many numbers you want in your password? \n"))
n_symbols = int(input("How many symbols you want in your password? \n"))

password_list = []

for i in range(n_letters):
    char = random.choice(letters)
    password_list += char
for x in range(n_numbers):
    num = random.choice(numbers)
    password_list += num
for y in range(n_symbols):
    symbol = random.choice(symbols)
    password_list += symbol

random.shuffle(password_list)
password=""

for x in password_list:
    password += x
    


print(password)