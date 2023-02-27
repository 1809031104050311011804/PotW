import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_weight():
    global weight

    try:
        weight = float(input("What is your weight (in lbs) on Earth?\n"))
        clear()
        user_planet()
    except:
        print("ERROR: INVALID INPUT\n")
        user_weight()


def user_planet():
    global planet

    try:
        planet = str(input("Please enter the name of the planet that you would like to weigh yourself on:\n")).upper()
    except:
        print("ERROR: INVALID INPUT")
        user_planet()
    
    if planet == "MERCURY" or planet == "VENUS" or planet == "MARS" or planet == "JUPITER" or planet == "SATURN" or planet == "URANUS" or planet == "NEPTUNE":
        user_planetary_weight()
    elif planet == "PLUTO":
        print("ERROR: PLUTO IS NOT A PLANET\n")
        user_planet()
    else:
        print("ERROR: PLANET NOT RECOGNIZED\n")
        user_planet()
    

def user_planetary_weight():
    if planet == "MERCURY":
        conversion_factor = 0.378
    elif planet == "VENUS":
        conversion_factor = 0.907
    elif planet == "MARS":
        conversion_factor = 0.377
    elif planet == "JUPITER":
        conversion_factor = 2.528
    elif planet == "SATURN":
        conversion_factor = 1.064
    elif planet == "URANUS":
        conversion_factor = 0.889
    elif planet == "NEPTUNE":
        conversion_factor = 1.125
    
    planetary_weight = round(weight*conversion_factor)

    clear()

    print("You would weigh {} lbs on {}.".format(planetary_weight, planet.capitalize()))
        

clear()
user_weight()