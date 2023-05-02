import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_bill():
    global bill

    try:
        bill = float(input("Enter the total cost of the bill ($):\n"))
        tip_calculator()
    except:
        print("ERROR: INVALID INPUT\n")
        user_bill()


def tip_calculator():
    tip_25 = bill * 0.25
    tip_20 = bill * 0.20
    tip_15 = bill * 0.10

    clear()

    print("Total Bill: \t${:0.2f}\n\n25% Tip: \t${:0.2f}\n20% Tip: \t${:0.2f}\n15% Tip: \t${:0.2f}\n".format(bill, tip_25, tip_20, tip_15))


clear()
user_bill()