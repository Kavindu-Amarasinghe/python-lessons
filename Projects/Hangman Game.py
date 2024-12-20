import random
word_list = ["apple", "banana", "cherry"]
chosen_word = random.choice(word_list)

print(chosen_word)

display = []

for letter in range(len(chosen_word)):
    display += '_'
print(display)

guessed_letter = input("Guess a letter: ")

for letter in chosen_word:
    if letter == guessed_letter:
        print("Match")
    else:
        print("No Match")

# print("Welcome to Hangman")
# print("You have only 6 guesses taken.")