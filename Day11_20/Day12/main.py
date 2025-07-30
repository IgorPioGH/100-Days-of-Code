import random
from art import logo
# variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# functions
def checking_guess(guess,result, turns):
    if guess > result:
        print(f"{guess} is to high")
        return turns - 1
    elif guess < result:
        print(f"{guess} is to low")
        return turns - 1
    else:
        print(f"Congrats you win! The answer was {result}")



def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if level == 'easy':
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS
    return turns

def receive_guess():
    guess = int(input("Try a number between 1 and 100: "))
    return guess

# Game rule
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Correct answer is {answer}")

    turns = set_difficulty()

    # Let the user guess a number
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining")
        # Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = checking_guess(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

# more rounds
while input("Do you want to play the guess the number game? 'y' or 'n': ").lower() == 'y':
    play_game()