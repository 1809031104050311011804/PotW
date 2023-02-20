import os
import time


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def time_teller():
    user_enter = input("Hit enter to check the current time.\n")

    if user_enter == "":
        current_time = time.ctime()
        print("The current time is:\n{}\n".format(current_time))
    else:
        print("ERROR: INVALID INPUT\n")
        time_teller()


clear()
time_teller()