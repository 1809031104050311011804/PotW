#Some of this code is sourced from:
##https://gist.github.com/bcooksey/90fc3409ca63c652dcfd9769b7cd0314


import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_distance():
    global distance

    try:
        distance = float(input("Distance traveled [mi]:\n"))
        clear()
        user_time()
    except:
        print("ERROR: INVALID INPUT\n")
        user_distance()


def user_time():
    global time, time_hours, time_minutes, time_seconds

    time = input("Time [HH:MM:SS]:\n")

    if time.count(":") == 2:
        time_hours, time_minutes, time_seconds = time.split(":")
        clear()
        pace_calculator()
    else:
        print("ERROR: INVALID INPUT\n")
        user_time()


def pace_calculator():
    total_seconds = (int(time_hours)*3600) + (int(time_minutes)*60) + int(time_seconds)

    seconds_per_mile = float(total_seconds) / distance
    pace_minutes = int(seconds_per_mile / 60)
    pace_seconds = int(seconds_per_mile - (pace_minutes*60))

    print("Pace:\n{} minutes and {} seconds per mile\n".format(pace_minutes, pace_seconds))


clear()
user_distance()