weight = int(input("Enter Weight in Kg: "))
height = int(input("Enter Height in Meter: "))

BMI = weight / (height * height)


if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI < 25:
    print("You are normal")
elif BMI >= 25 and BMI < 30:
    print("You are obese")
elif BMI >= 30 and BMI < 40:
    print("You are overweight")
else:
    print(f"Your BMI is {BMI} and you are  ")