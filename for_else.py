tuple1 = (2,56,34,3,5,1)

# for i in tuple1:
#     print(i)
#     if i == 5:
#         break
# else:
#     print("Loop successfully completed")
for i in tuple1:
    if i%6 == 0:
        print(i)
        break
else:
    print("There is no number divisible by 6")