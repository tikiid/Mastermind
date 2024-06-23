# Mastermind Game
 
Welcome to the Mastermind game! This is a console-based implementation of the classic code-breaking game, written in Python.

## Game Description

Mastermind is a code-breaking game for two players. One player (in this case, the computer) creates a secret combination of four colors, and the other player (you) tries to guess the combination within 10 attempts. The computer provides feedback on each guess, indicating whether the colors are correct and in the right position.

## Features

- The game uses six colors: Red (R), Blue (B), Orange (O), Green (G), Yellow (Y), and Purple (P).
- The secret combination consists of four colors.
- Feedback for each guess:
  - `!` indicates the color is correct and in the right position.
  - `?` indicates the color is correct but in the wrong position.
  - `-` indicates the color is not in the secret combination.
- The game displays a board showing all attempts.
- Option to restart the game after each round.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Running the Game
Run the Python script to start the game:

python mastermind.py

## How to Play
- Start the game by pressing Enter.
- Enter your guess for the secret combination in the format RYBG (using the color initials).
- The game will provide feedback for each guess.
- Continue guessing until you either guess the secret combination or use all 10 attempts.
- After the game ends, you can choose to play again or exit.

## Author 
Thibaut Schweitzer
