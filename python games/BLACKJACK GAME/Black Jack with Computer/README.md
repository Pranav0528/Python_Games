Blackjack Game
Overview
This repository contains a simple implementation of a text-based Blackjack game in Python. The game uses the console for interaction and includes basic functionalities such as dealing cards, calculating scores, and determining the winner.

*** Game Flow *** 

1. Start:
  User initiates the game.

2. Initialize Hands:
  Two players (Player 1 and Player 2) are initialized with two cards each.

3. Player 1's Turn:
  Player 1 is prompted to decide whether to hit or stand.
  If hit, a new card is added to Player 1's hand.
  If stand or if the total score is 21, the turn ends.

4. Player 2's Turn:
  Player 2 is prompted to decide whether to hit or stand.
  If hit, a new card is added to Player 2's hand.
  If stand or if the total score is 21, the turn ends.

5. Result Calculation:
  Final hands and total scores for both players are displayed.

6. Compare and Display Winner:
  The scores of both players are compared.
  The winner or a draw is displayed based on the comparison.

7. Game Loop Decision:
  User is asked if they want to play another round.
  If 'y', go back to step 2 (Initialize Hands).
  If 'n', end the game.

8. End:
  Game ends.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
