import os
from datetime import date


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_dob():
    global dob

    dob = input("Enter your date of birth (MM/DD/YYYY):\n")

    try:
        dob = dob.split("/")
        
        dob_year = int(dob[2])
        dob_month = int(dob[0])
        dob_day = int(dob[1])
        
        dob = date(dob_year, dob_month, dob_day)
        
        clear()
        age_calculator()
    except:
        print("ERROR: INVALID INPUT\n")
        user_dob()


def age_calculator():
    today = date.today()
    
    age = today - dob

    age_years = age.days // 365
    age_months = (age.days % 365) // 30
    age_days = (age.days % 365) % 30

    print("You are {} years, {} months, and {} days old.\n".format(age_years, age_months, age_days))


def main():
    clear()
    user_dob()


main()