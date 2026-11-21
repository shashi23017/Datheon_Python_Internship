# Task 1 – Hangman Word Guessing Game

## Project Description

This project is a simple console-based Hangman game developed using Python as part of the Datheon Python Programming Internship.
The player needs to guess a randomly selected secret word by entering one letter at a time. The player has a maximum of six incorrect guesses before the game ends.

## Features

- Randomly selects a word from `wordList.txt`.
- Displays the secret word using underscores (`_`).
- Allows the player to guess one letter at a time.
- Tracks previously guessed letters.
- Prevents duplicate guesses.
- Displays Hangman ASCII art for each incorrect guess.
- Provides a maximum of 6 incorrect attempts.
- Displays a winning message when the player guesses the word correctly.
- Displays a game-over message when all attempts are used.

## Technologies Used

- Python
- `random` module
- `os` module

## Project Structure

```text
Datheon_Python_Programming_Internship/
├── Task1/
│   ├── hangman.py
│   └── wordList.txt
└── README.md
```
