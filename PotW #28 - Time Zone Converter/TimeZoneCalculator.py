import os
from datetime import datetime, timedelta


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_input():
    global source_time, converted_time

    try:
        source_time = input("Source Time (00:00 XXX):\n").split(" ")
        source_time[0] = datetime.strptime(source_time[0], "%H:%M")
        source_time[1] = source_time[1].upper()

        converted_time = [""] * 2
        converted_time[1] = input("\nDesired Time Zone (XXX):\n")
        converted_time[1] = converted_time[1].upper()
    except:
        print("ERROR: INPUT NOT VALID\n")
        user_input()

    time_converter()


def time_converter():
    if source_time[1] == "PST":
        if converted_time[1] == "MST":
            time_factor = +1
        elif converted_time[1] == "CST":
            time_factor = +2
        elif converted_time[1] == "EST":
            time_factor = +3
    elif source_time[1] == "MST":
        if converted_time[1] == "PST":
            time_factor = -1
        elif converted_time[1] == "CST":
            time_factor = +1
        elif converted_time[1] == "EST":
            time_factor = +2
    elif source_time[1] == "CST":
        if converted_time[1] == "PST":
            time_factor = -2
        elif converted_time[1] == "MST":
            time_factor = -1
        elif converted_time[1] == "EST":
            time_factor = +1
    elif source_time[1] == "EST":
        if converted_time[1] == "PST":
            time_factor = -3
        elif converted_time[1] == "MST":
            time_factor = -2
        elif converted_time[1] == "CST":
            time_factor = -1
    else:
        print("ERROR: CONVERSION NOT SUPPORTED\n")
        user_input()
    
    converted_time[0] = source_time[0] + timedelta(hours=time_factor)

    print("\nConverted Time:\n{:02d}:{:02d} {}\n".format(converted_time[0].hour, converted_time[0].minute, converted_time[1]))


def main():
    clear()
    user_input()


main()