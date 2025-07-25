import random
import hangman_art
import hangman_words

stages = hangman_art.stages
word_list = hangman_words.word_list

chosen_word = random.choice(word_list)

placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

previous_guess = []

game_over = False
life = 6

while life > 0 and not game_over:

    guess = input("Guess a letter: ").lower()
    display = ""

    if guess not in chosen_word and guess not in previous_guess:
        life -= 1
        print('You lose 1 life')
        print(f"****************************{life}/6 LIVES LEFT****************************")

    elif guess in previous_guess:
        print(f'You already tried the letter: {guess}')
    previous_guess.append(guess)

    for letter in chosen_word:
        if letter == guess or letter in previous_guess:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        game_over = True
        print("You won!")

    print(stages[life])
    print(display)

if life == 0:
    print("You Lose!")
    print(f"The word was: {chosen_word}")

