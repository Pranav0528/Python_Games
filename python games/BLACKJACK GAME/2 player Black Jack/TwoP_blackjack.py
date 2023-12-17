import random
import os
from art import logo

def dealcard():
    """Deals a random card from a deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def cal_score(cards):
    """Take a list of cards as input and return a score from the list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and (11 in cards):
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player1_score, player2_score):
    if player1_score == player2_score:
        return "It's a Draw!!"
    elif player2_score == 0:
        return "Player 2 has Blackjack. Player 1 Lost."
    elif player1_score == 0:
        return "Player 1 Won with Blackjack!!"
    elif player1_score > 21:
        return "Player 1 went over, Player 2 Wins :("
    elif player2_score > 21:
        return "Player 2 went over, Player 1 Wins!!"
    elif player1_score > player2_score:
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"

def player_turn(player_name, player_cards):
    isPlayerOver = False

    while not isPlayerOver:
        player_score = cal_score(player_cards)
        print(f"{player_name}'s cards are {player_cards} and the total score is {player_score}")

        if player_score == 0 or player_score > 21:
            isPlayerOver = True
        else:
            user_deal_appeal = input(f"{player_name}, type 'y' to get another card or 'n' to pass: ")
            if user_deal_appeal == "y":
                player_cards.append(dealcard())
            else:
                isPlayerOver = True

def play_game():
    print(logo)
    player1_cards = []
    player2_cards = []

    for _ in range(2):
        player1_cards.append(dealcard())
        player2_cards.append(dealcard())

    # Player 1's turn
    player_turn("Player 1", player1_cards)

    # Player 2's turn
    player_turn("Player 2", player2_cards)

    print(f"Player 1's Final Hand: {player1_cards} and total score: {cal_score(player1_cards)}")
    print(f"Player 2's Final Hand: {player2_cards} and total score: {cal_score(player2_cards)}")
    print(compare(cal_score(player1_cards), cal_score(player2_cards)))

# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()
