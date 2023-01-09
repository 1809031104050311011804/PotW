import os
import time


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_net_monthly_income():
    global net_monthly_income

    try:
        net_monthly_income = float(input("What is your net monthly income? ($)\n"))
    except:
        print("ERROR: INVALID RESPONSE\n")
        user_net_monthly_income()

    clear()


def user_spending_habits():
    global spending_habits, spending_habits_factor

    spending_habits = input("How would you describe your spending habits? (Conservative/Mild/Frugal)\n").upper()

    if spending_habits == "CONSERVATIVE" or spending_habits == "MILD" or spending_habits == "FRUGAL":
        clear()
    else:
        print("ERROR: INVALID RESPONSE\n")
        user_spending_habits()

    if spending_habits == "CONSERVATIVE":
        spending_habits_factor = 0.1
    elif spending_habits == "MILD":
        spending_habits_factor = 0.0
    elif spending_habits == "FRUGAL":
        spending_habits_factor = -0.1


def user_profile():
    clear()
    
    user_net_monthly_income()
    user_spending_habits()

    print("Calculating your monthly budget...\n")
    time.sleep(1)

    monthly_budget_calculator()


def monthly_budget_calculator():
    clear()

    housing         = net_monthly_income * (0.25)
    food            = net_monthly_income * (0.15)
    savings         = net_monthly_income * (0.25 + spending_habits_factor)
    necessities     = net_monthly_income * (0.15)
    discretionary   = net_monthly_income * (0.20 - spending_habits_factor)

    print("Net Monthly Income: ${}\n".format(round(net_monthly_income, 2)))
    
    print("Housing\t\t (25%):\t ${}".format(round(housing, 2)))
    print("Food\t\t (15%):\t ${}".format(round(food, 2)))
    print("Savings\t\t ({}%):\t ${}".format(round(100*(0.25+spending_habits_factor)), round(savings, 2)))
    print("Necessities\t (15%):\t ${}".format(round(necessities, 2)))
    print("Discretionary\t ({}%):\t ${}".format(round(100*(0.20-spending_habits_factor)), round(discretionary, 2)))

    print("")


user_profile()













