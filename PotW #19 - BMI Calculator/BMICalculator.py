import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_weight():
    global weight
    
    try:
        weight = float(input("Enter your weight (in lbs):\n"))
        clear()
        user_height()
    except:
        print("ERROR: INVALID INPUT\n")
        user_weight()


def user_height():
    global height

    try:
        height = float(input("Enter your height (in in.):\n"))
        clear()
        bmi_calculator()
    except:
        print("ERROR: INVALID INPUT\n")
        user_height()


def bmi_calculator():
    bmi = (weight/2.2050) / ((height*0.0254)**2)

    print("BMI = {:0.2f}".format(bmi))


clear()
user_weight()