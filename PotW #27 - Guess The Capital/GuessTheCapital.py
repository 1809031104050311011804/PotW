import os
import random


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def game_difficulty():
    global guesses_remaining

    difficulty = input("Which difficulty would you like to play on? (Easy/Medium/Hard/Extreme)\n").upper()
    
    if difficulty == "EASY":
        guesses_remaining = 10
    elif difficulty == "MEDIUM":
        guesses_remaining = 5
    elif difficulty == "HARD":
        guesses_remaining = 3
    elif difficulty == "EXTREME":
        guesses_remaining = 1
    else:
        print("ERROR: INVALID DIFFICULTY\n")
        game_difficulty()
    
    clear()
    random_state()
    random_state_capital()
    user_guess()


def random_state():
    global state, random_number

    states =    ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
                "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
                "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
                "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
                "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    random_number = random.randint(0, len(states))
    
    state = states[random_number].upper()

    random_state_capital()


def random_state_capital():
    global capital
    
    capitals =  ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento",
                "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta",
                "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines",
                "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis",
                "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City",
                "Helena", "Licoln", "Carson City", "Concord", "Trenton",
                "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus",
                "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia",
                "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier",
                "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

    capital = capitals[random_number].upper()


def user_guess():
    global capital_guess

    capital_guess = str(input("What is the capital of {}?\n".format(state)).upper())

    game_tracker()


def game_tracker():
    global guesses_remaining
    
    guesses_remaining -= 1

    if capital_guess == capital:
        print("\nYou are correct! The capital of {} is {}.".format(state, capital))
        game_replay()
    
    else:
        if guesses_remaining == 0:
            print("\nYou lose! You failed to guess the capital of {} with your available guesses.".format(state))
            game_replay()
        else:
            print("\nYou are incorrect! The capital of {} is not {}.\nGUESSES REMAINING: {}\n".format(state, capital_guess, guesses_remaining))
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