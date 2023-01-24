import os
import time


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def supported_conversions():
    clear()

    print("This program currently supports the following conversions:")
    print("(1) Feet\t-->\tMeters")
    print("(2) Meters\t-->\tFeet")
    print("(3) Miles\t-->\tKilometers")
    print("(4) Kilometers\t-->\tMiles")
    print("(5) Gallons\t-->\tLiters")
    print("(6) Liters\t-->\tGallons")
    print("")

    user_select()


def user_select():
    global selection, input_units, output_units

    try:
        selection = int(input("Enter the conversion that you would like to perform:\n"))
    except:
        print("ERROR: INVALID INPUT\n")
        user_select()

    if selection == 1:
        input_units = "ft"
        output_units = "m"
    elif selection == 2:
        input_units = "m"
        output_units = "ft"
    elif selection == 3:
        input_units = "mi"
        output_units = "km"
    elif selection == 4:
        input_units = "km"
        output_units = "mi"
    elif selection == 5:
        input_units = "gal"
        output_units = "L"
    elif selection == 6:
        input_units = "L"
        output_units = "gal"
    else:
        print("ERROR: CONVERSION NOT SUPPORTED\n")
        user_select()

    clear()
    user_input()


def user_input():
    global input_value

    try:
        input_value = float(input("Enter the value that you would like to convert from {} to {}:\n".format(input_units, output_units)))
    except:
        print("ERROR: INVALID INPUT\n")
        user_input()
    
    input_convert()


def input_convert():
    global output_value
    
    if selection == 1:
        conversion_factor = 0.3048
    elif selection == 2:
        conversion_factor = 3.2810
    elif selection == 3:
        conversion_factor = 1.6090
    elif selection == 4:
        conversion_factor = 0.6214
    elif selection == 5:
        conversion_factor = 3.7850
    elif selection == 6:
        conversion_factor = 0.2642

    output_value = input_value * conversion_factor

    output()


def output():
    print("\n{:0.4f} {} = {:0.4f} {}".format(round(input_value,3), input_units, output_value, output_units))

    time.sleep(2)
    convert_again()


def convert_again():    
    again = input("\nWould you like to convert another value? (Y/N)\n").upper()

    if again == "Y":
        supported_conversions()
    elif again == "N":
        clear()
        exit()
    else:
        print("ERROR: INVALID INPUT")
        convert_again()


supported_conversions()
