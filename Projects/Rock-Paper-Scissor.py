import random
rock = "🪨"
paper = "📃"
scissor = "✂️"

game_icon = [rock, paper, scissor]

User_Choice = int(input("Enter Your Choice: Type 0 for 🪨,Type 1 for 📃,Type 2 for ✂️: "))

if User_Choice >= 3 or User_Choice < 0:
    print("Invalid Choice")
else:
    print("Your choice "+game_icon[User_Choice])


computer_choice = random.randint(0,2)
print("Computer chose: 2"+game_icon[computer_choice])


if(computer_choice == User_Choice):
    print("It's a draw")
elif(computer_choice == 0 and User_Choice == 2):
    print("You Lose,Computer Win 🏆")
elif(User_Choice == 0 and computer_choice == 2):
    print("You Win. You Win 🏆")
elif(computer_choice > User_Choice):
    print("You lose.Computer Win 🏆")
elif(computer_choice < User_Choice):
    print("Computer lose. You Win 🏆")
