print("---PIZZA ORDER PROGRAM--------")

size = input("What is size Pizza You want(S/M/L): ")
bill = 0;

if size == "S" or size == "s":
    bill = bill+100;
    print("Small Pizza price is 100 RS")

elif size == "M" or size == "m":
    bill = bill+200;
    print("Medium Pizza price is 200 RS")

elif size == "L" or size == "l":
    bill = bill+300;
    print("Large Pizza price is 300 RS")

add_pepperoni = input("Do you want pepperoni(Y/N)? ")
if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
        bill = bill+30;
    elif size == "M" or size == "m":
        bill = bill+50;
    elif size == "L" or size == "l":
        bill = bill+70;
extra_cheese = input("Do you want extra cheese(Y/N)? ")
if extra_cheese == "Y" or extra_cheese == "y":
    if size == "S" or size == "s":
        bill = bill+40;
    elif size == "M" or size == "m":
        bill = bill+50;
    elif size == "L" or size == "l":
        bill = bill+60;
print(bill)