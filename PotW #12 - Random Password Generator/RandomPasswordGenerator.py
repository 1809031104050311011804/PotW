import os
import random
import string
import time


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def password_generator():
    global password

    password_length = random.randint(8,16)
    password = [None] * password_length

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    letters = list(string.ascii_lowercase)

    for i in range(len(password)):
        character_random = random.randint(1,3)
        
        if character_random == 1:
            symbol_random = random.randint(1, len(symbols)-1)
            password[i] = symbols[symbol_random]

        elif character_random == 2:
            letter_random = random.randint(1, len(letters)-1)
            case_random = random.randint(0, 1)
            if case_random == 0:
                password[i] = letters[letter_random].lower()
            elif case_random == 1:
                password[i] = letters[letter_random].upper()
        
        elif character_random == 3:
            number_random = random.randint(0,9)
            password[i] = number_random
        
    password = ''.join(map(str, password))

    password_show()
            

def password_show():
    clear()

    print("Password:\n{}".format(password))

    time.sleep(2)
    generate_again()


def generate_again():
    again = input("\nWould you like to generate another password? (Y/N)\n").upper()

    if again == "Y":
        password_generator()
    elif again == "N":
        clear()
        exit()
    else:
        print("ERROR: INVALID RESPONSE")
        generate_again()


password_generator()