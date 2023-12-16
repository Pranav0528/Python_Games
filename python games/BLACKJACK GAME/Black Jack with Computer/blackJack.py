import random
import os
from art import logo
def dealcard():
    """Deals a random card from a deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def cal_score(cards):
    """take list of cards as input and return a score from the list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and (11 in cards):
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(uScore, cScore):
    if uScore == cScore:
        return "Its a Draw!! "
    elif cScore == 0:
        return "Your Lost. opponent has BlackJack"
    elif uScore == 0: 
        return "You Won with BlackJack!!"
    elif uScore > 21:
        return "You went over, You Lose :("
    elif cScore > 21:
        return " Your Opponent went over, You Win!!"
    elif uScore > cScore:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    isGameOver = False

    for _ in range(2):
        user_cards.append(dealcard())
        computer_cards.append(dealcard())

    while not(isGameOver):
        uScore = cal_score(user_cards)
        cScore = cal_score(computer_cards)
        print(f"Your cards are {user_cards} and your total score is {uScore} \n Computer's first card is {computer_cards[0]}")

        if uScore == 0 or cScore == 0 or uScore > 21:
            isGameOver = True
        else:
            user_deal_appeal = input("Type 'y' to get another card or type 'n' to pass ")
            if(user_deal_appeal == "y"):
                user_cards.append(dealcard())
            else:
                isGameOver = True 

    while cScore != 0 and cScore < 21:
        computer_cards.append(dealcard())
        cScore = cal_score(computer_cards)

    print(f"Your Final Hand : {user_cards} and your total score: {uScore} ")
    print(f"Computer's Final Hand : {computer_cards} and computer total score is: {cScore}")
    print(compare(uScore, cScore))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("cls")
  play_game()