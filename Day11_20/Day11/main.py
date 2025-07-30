import random
from art import logo
# funcoes
def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if  sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)

def compare_scores(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "You win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose"

def play_game():
    # variables
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    # printting logo
    print(logo)
    # First hand
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Game rule
    # User loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer loop
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}. Final score: {user_score}")
    print(f"Computer final hand: {computer_cards}. Final_socre: {computer_score}")
    print(compare_scores(user_score, computer_score))


while input("Do you want to play another game of Blackjack? 'y' or 'n': ") == 'y':
    print("\n"*20)
    play_game()