import os
import random
import time


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def game_difficulty():
    global guesses_remaining

    difficulty = input("Which difficulty would you like to play on? (Easy/Medium/Hard/Extreme)\n").upper()
    
    if difficulty == "EASY":
        guesses_remaining = 15
    elif difficulty == "MEDIUM":
        guesses_remaining = 10
    elif difficulty == "HARD":
        guesses_remaining = 5
    elif difficulty == "EXTREME":
        guesses_remaining = 1
    else:
        print("ERROR: INVALID DIFFICULTY\n")
        game_difficulty()

    clear()
    number_generator()
    user_guess()


def number_generator():
    global number_correct
    number_correct = random.randint(0, 100)


def user_guess():
    global number_guess

    try:
        number_guess = int(input("Guess a number between 0 and 100:\n"))
    except:
        print("ERROR: NON-INTEGER GUESS\n")
        user_guess()

    if number_guess < 0 or number_guess > 100:
        print("ERROR: GUESS OUTSIDE OF RANGE\n")
        user_guess()

    guess_accuracy()
    game_tracker()


def guess_accuracy():
    global guess_difference, guess_relativity

    guess_difference = number_correct - number_guess

    if guess_difference > 0:
        guess_relativity = "lower"
    elif guess_difference < 0:
        guess_relativity = "higher"


def game_tracker():
    global guesses_remaining
    
    guesses_remaining -= 1

    if guess_difference == 0:
        print("\nYou guessed the correct number ({}) with {} guesses remaining. You win!".format(number_correct, guesses_remaining))
        
        time.sleep(4)
        game_replay()
    
    else:
        if guesses_remaining == 0:
            print("\nYou failed to guess the correct number ({}) with your available guesses. You lose!".format(number_correct))
            
            time.sleep(4)
            game_replay()
        
        print("\nYour guess ({}) was {} than the correct number.\nGUESSES REMAINING: {}\n".format(number_guess, guess_relativity, guesses_remaining))

    user_guess()


def game_replay():
    play_again = input("\nWould you like to play again? (Y/N)\n").upper()

    if play_again == "Y":
        clear()
        game_difficulty()
    elif play_again == "N":
        clear()
        exit()
    else:
        print("ERROR: INVALID RESPONSE")
        game_replay()


clear()
game_difficulty()