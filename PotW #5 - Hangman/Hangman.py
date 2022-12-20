import random
import pandas as pd
import os
import string


def introduction():
    print("\nWelcome to Hangman!")
    print("\nIn this game, you will be asked to guess a random word by guessing one letter at a time. If you are unable to guess the word before the hangman is complete, then you lose.")

    ready()


def ready():
    player_ready = input("\nAre you ready to continue? (Y/N)\n")
    
    if player_ready == "Y":
        clear()
        reset()
    elif player_ready == "N":
        exit()
    else:
        print("ERROR: INVALID RESPONSE")
        ready()
 

def reset():
    global hangman, guesses, g
    
    hangman =   [" ", " ", " ", " ", " ", " ", " "]
    guesses =   [" ", " ", " ", " ", " ", " ", " "]
    g       =   0

    difficulty()


def difficulty():
    global player_difficulty
    
    player_difficulty = input("\nWhat difficulty would you like to play on? (Easy/Medium/Hard)\n")
    
    if player_difficulty == "Easy" or player_difficulty == "Medium" or player_difficulty == "Hard":
        word()
    else:
        print("ERROR: INVALID RESPONSE")
        difficulty()


def word():
    global correct_word, guessed_word, tracked_word
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    file_path = os.getcwd()
    
    word_bank = pd.read_excel(os.path.join(file_path, "Word Bank.xlsx"))
    
    row = random.randint(0, len(word_bank)-1)

    if player_difficulty == "Easy":
        column = 0
        correct_word = word_bank.iloc[row, column]
    if player_difficulty == "Medium":
        column = 1
        correct_word = word_bank.iloc[row, column]
    if player_difficulty == "Hard":
        column = 2
        correct_word = word_bank.iloc[row, column]

    correct_word = correct_word.upper()

    guessed_word = ["_ "]   * len(correct_word)

    tracked_word = [""]     * len(correct_word)

    update()


def guess():
    global player_guess
    
    alphabet = list(string.ascii_uppercase)

    player_guess = input("\nWhat letter would you like to guess?\n").upper()
    
    if player_guess in tracked_word or player_guess in guesses:
        print("ERROR: LETTER ALREADY GUESSED")
        guess()
    elif player_guess in alphabet:
        result()
    else:
        print("ERROR: INVALID RESPONSE")
        guess()


def result():
    global g
    
    if player_guess in correct_word:
        location = 0
        while location < len(correct_word):
            location = correct_word.find(player_guess, location)
            if location == -1:
                break
            guessed_word[location] = player_guess + " "
            tracked_word[location] = player_guess
            location += 1
    elif hangman[0] == " " and player_guess not in correct_word:
        hangman[0] = "O"
        guesses[g] = player_guess
        g += 1
    elif hangman[1] == " " and player_guess not in correct_word:
        hangman[1] = "|"
        guesses[g] = player_guess
        g += 1
    elif hangman[2] == " " and player_guess not in correct_word:
        hangman[2] = "\\"
        guesses[g] = player_guess
        g += 1
    elif hangman[3] == " " and player_guess not in correct_word:
        hangman[3] = "/"
        guesses[g] = player_guess
        g += 1
    elif hangman[4] == " " and player_guess not in correct_word:
        hangman[4] = "/"
        guesses[g] = player_guess
        g += 1
    elif hangman[5] == " " and player_guess not in correct_word:
        hangman[5] = "\\"
        guesses[g] = player_guess
        g += 1

    update()


def update():
    clear()
    
    updated_word = "".join(guessed_word)

    print("    ______                   ")
    print("   |/     |                  ")
    print("   |      {}                 ".format(hangman[0]))
    print("   |     {}{}{}              ".format(hangman[2], hangman[1], hangman[3]))
    print("   |     {} {}               ".format(hangman[4], hangman[5]))
    print("___|___                      ")
    
    print("\n{}                         ".format(updated_word))
    
    print("\nGuesses: {} {} {} {} {} {} ".format(guesses[0], guesses[1], guesses[2], guesses[3], guesses[4], guesses[5]))

    tracker()


def tracker():
    if tracked_word == [*correct_word]:
        print("\nYou won!")
        replay()
    if hangman[5] != " ":
        print("\nYou lost. The correct word was {}.".format(correct_word))
        replay()
    else:
        guess()


def replay():
    player_replay = input("\nWould you like to play again? (Y/N)\n")

    if player_replay == "Y":
        clear()
        reset()
    elif player_replay == "N":
        exit()
    else:
        print("ERROR: INVALID RESPONSE")
        replay()


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


introduction()
