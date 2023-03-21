import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_wage_type():
    global wage_type
    
    wage_type = input("Are you an hourly or salary employee?\n").upper()

    if wage_type == "HOURLY":
        clear()
        user_hourly_wage()
    elif wage_type == "SALARY":
        clear()
        user_annual_salary()
    else:
        print("ERROR: WAGE TYPE NOT SUPPORTED\n")
        user_wage_type()


def user_hourly_wage():
    global hourly_wage
    
    try:
        hourly_wage = float(input("What is your hourly wage?\n"))
        clear()
        user_average_hours_worked()
    except:
        print("ERROR: INVALID INPUT\n")
        user_hourly_wage()


def user_average_hours_worked():
    global average_hours_worked
    
    try:
        average_hours_worked = int(input("How many hours do you work per week (on average)?\n"))
        clear()
        gross_paycheck_calculator()
    except:
        print("ERROR: INVALID INPUT\n")
        user_average_hours_worked()
    

def user_annual_salary():
    global annual_salary

    try:
        annual_salary = int(input("What is your annual salary?\n"))
        clear()
        gross_paycheck_calculator()
    except:
        print("ERROR: INVALID INPUT\n")
        user_annual_salary()
    

def gross_paycheck_calculator():
    global weekly_paycheck, bi_weekly_paycheck, monthly_paycheck
    
    if wage_type == "HOURLY":
        weekly_paycheck = hourly_wage * average_hours_worked
    elif wage_type == "SALARY":
        weekly_paycheck = annual_salary / 52

    bi_weekly_paycheck = weekly_paycheck * 2
    monthly_paycheck = weekly_paycheck * 4

    gross_paycheck()


def gross_paycheck():
    if wage_type == "HOURLY":
        print("By working {:0.0f} hours/week at an hourly wage of ${:0.2f}/hour, you can expect to have a gross pay of:\n".format(average_hours_worked, hourly_wage))
        print("${:0.2f} every week".format(weekly_paycheck))
        print("${:0.2f} every 2 weeks".format(bi_weekly_paycheck))
        print("${:0.2f} every month\n".format(monthly_paycheck))
    elif wage_type == "SALARY":
        print("With an annual salary of ${:0.0f}, you can expect to have a gross pay of:\n".format(annual_salary))
        print("${:0.2f} every week".format(weekly_paycheck))
        print("${:0.2f} every 2 weeks".format(bi_weekly_paycheck))
        print("${:0.2f} every month\n".format(monthly_paycheck))


clear()
user_wage_type()