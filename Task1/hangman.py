
import random
import os

file_path = os.path.join(os.path.dirname(__file__), "wordList.txt")

with open(file_path, "r") as file:
    words = file.read().splitlines()

secret_word = random.choice(words).lower()

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

hangman_art = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

while wrong_guesses < max_wrong_guesses:

    print(hangman_art[wrong_guesses])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_wrong_guesses - wrong_guesses)

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")

    elif guess in guessed_letters:
        print("You already guessed that letter.")

    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! YOU WIN!")
        print("The correct word is:", secret_word.upper())
        break

if wrong_guesses == max_wrong_guesses:
    print(hangman_art[wrong_guesses])
    print("\nGAME OVER!")
    print("The correct word was:", secret_word.upper())

print("Thank you for playing!")
