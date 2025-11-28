# Project title

Number Guessing Game

# Overview of the project
This project implements a simple command-line based Number Guessing Game. The objective is for the user to guess a randomly generated secret number within a specified range (0 to 100) and within a limited number of tries (5 guesses). The system provides hints (higher or lower) after each incorrect guess.

# Features
* Random Number Generation: A secret number is randomly generated between 0 and 100.

* Guess Limit: The user has a maximum of 5 attempts to guess the number.

* Hints: After an incorrect guess, the user is informed whether the secret number is greater or less than their guess.

* Win/Loss Outcome: Clearly displays a congratulatory message upon a correct guess or a loss message revealing the number after all attempts are exhausted.

* Replay Option: Allows the user to choose to play the game again.

# Technologies/tools used
* Programming Language: Python 3.14

* Modules: random module for number generation

# Steps to install & run the project
* Prerequisites: Ensure you have Python 3.x installed on your system.

* Download/Clone: Download the source-code.py file to your local machine.

* Execution: Open your terminal or command prompt, navigate to the directory where the file is saved, and run the following command:

* Play: Follow the on-screen instructions to enter your guesses.

# Instructions for testing
The game is interactive and can be tested manually: 

* Start the game by running the script.

* Test correct guessing: Enter numbers until you guess correctly within 5 tries. Verify the "CONGRATULATIONS!!!" message is displayed.

* Test incorrect guessing (loss): Intentionally guess wrong 5 times. Verify the "Sorry. You Lost" message and the correct number are displayed.

* Test hints: Verify that the messages "The number is less..." and "The number is greater..." appear correctly based on your guess relative to the secret number.

* Test replay: At the end of a game, enter 'y' to restart and 'n' to exit the program.


