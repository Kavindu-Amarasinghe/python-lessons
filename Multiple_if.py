height = int(input ("How tall are you? "))
total = 0

if height > 3:
    print("Can Ride")
    age = int(input("How old are you? "))
    if age < 12:
        print("Ticket Price is 150 Rs")
        total = total + 150
    if age < 12 and age <=18:
        print("Ticket Price is 250 Rs")
        total = total + 250
    if age > 18:
        print("Ticket Price is 500 Rs")
        total = total + 500

    want_photo= input("Do you want photo (Y/N)? ")
    if want_photo == "Y" or want_photo == "y":
        total = total + 50
        print("Your ticket price is", total)
    elif want_photo == "N" or want_photo == "n":
        total = total + 0
        print("Your ticket price is", total)
else:
    print("Sorry, you can't ride")
print("Bye")

