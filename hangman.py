import random

# List of predefined words
words = ["apple", "tiger", "chair", "robot", "plant"]

# Randomly choose a word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_attempts = 6

print("===================================")
print("      WELCOME TO HANGMAN GAME      ")
print("===================================")

while wrong_attempts > 0:

    display_word = ""

    # Show guessed letters and hide others
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly.")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Wrong guess
    if guess not in word:
        wrong_attempts -= 1
        print("Wrong guess!")
        print("Remaining attempts:", wrong_attempts)

else:
    print("\nGame Over!")
    print("The correct word was:", word)

print("Thank you for playing!")
