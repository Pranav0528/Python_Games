Blackjack Game
Overview
This repository contains a simple implementation of a text-based Blackjack game in Python. The game uses the console for interaction and includes basic functionalities such as dealing cards, calculating scores, and determining the winner.

Files
blackJack.py: The main script containing the Blackjack game logic.
art.py: A separate file containing ASCII art for the game's logo.
How to Play
Run the blackJack.py script in a Python environment.
Follow the prompts to play a game of Blackjack.
You will be dealt two initial cards, and you have the option to draw additional cards to improve your hand.
The game will determine the winner based on the final scores of the player and the computer.

Dependencies
Python 3.x

The art library for ASCII art. Install it using the following command:
pip install art

How to Run
Execute the following command in your terminal or command prompt:
blackJack.py

Game Rules
Face cards have a value of 10.
Aces can be either 1 or 11, whichever benefits the hand more.
The goal is to get as close to 21 as possible without exceeding it.
If your initial two cards sum to 21, you get a Blackjack.
The computer opponent follows a simple strategy of drawing cards until its total is at least 17.
Note
This is a basic implementation, and the game logic can be further extended or modified for additional features or variations.

Feel free to contribute or use the code as a starting point for your own projects!
