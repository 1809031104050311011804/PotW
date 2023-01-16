import os
import random
import time


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_shake():
    clear()

    shake = input("Hit enter to shake the Magic 8-Ball.")

    if shake == "":
        magic_8_ball_result()
    else:
        print("ERROR: INVALID RESPONSE")
        user_shake


def magic_8_ball_responses():
    global responses

    responses = [  "It is certain.",
                        "It is decidedly so.",
                        "Without a doubt.",
                        "Yes, definitely.",
                        "You may rely on it.",
                        "As I see it, yes.",
                        "Most likely.",
                        "Outlook good.",
                        "Yes.",
                        "Signs point to yes.",
                        "Reply hazy, try again.",
                        "Ask again later.",
                        "Better not tell you now.",
                        "Cannot predict now.",
                        "Concentrate and ask again.",
                        "Don't count on it.",
                        "My reply is no.",
                        "My sources say no.",
                        "Outlook not so good.",
                        "Very doubtful."]


def magic_8_ball_result():
    clear()
    magic_8_ball_responses()

    print("Shaking the Magic 8-Ball...\n")
    time.sleep(random.randint(1,6))

    responses_index = random.randint(0,len(responses)-1)
    print(responses[responses_index])

    time.sleep(3)
    user_shake_again()


def user_shake_again():
    shake_again = input("\nWould you like to shake the Magic 8-Ball again? (Y/N)\n").upper()

    if shake_again == "Y":
        magic_8_ball_result()
    elif shake_again == "N":
        clear()
        exit()
    else:
        print("ERROR: INVALID RESPONSE")
        user_shake_again()


user_shake()