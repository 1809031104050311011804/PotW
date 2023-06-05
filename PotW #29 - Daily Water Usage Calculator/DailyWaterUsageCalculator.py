import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_habits():
    global shower_rate, bathroom_rate, laundry_rate, dishwasher_rate
    
    print("On any given day, enter the average number of times that you do the following:\n")

    try:
        shower_rate     =   float(input("\nTake a shower:\n"))
        bathroom_rate   =   float(input("\nUse the bathroom:\n"))
        laundry_rate    =   float(input("\nDo laundry:\n"))
        dishwasher_rate =   float(input("\nRun the dishwasher:\n"))
    except:
        print("ERROR: INVALID INPUT\n")
        user_habits()


def daily_water_usage_calculator():
    shower_usage        =   16      #gallons per shower
    toilet_usage        =   1.6     #gallons per flush
    sink_usage          =   0.8     #gallons per hand-wash
    laundry_usage       =   20      #gallons per load of laundry
    dishwasher_usage    =   4       #gallons per dishwasher cycle

    daily_water_usage   =   (shower_rate*shower_usage) + (bathroom_rate*toilet_usage) + (bathroom_rate*sink_usage) + (laundry_rate*laundry_usage) + (dishwasher_rate*dishwasher_usage)
    
    print("Based on your responses, you use {:0.1f} gallons of water per day.\n".format(daily_water_usage))


def main():
    clear()
    user_habits()
    clear()
    daily_water_usage_calculator()


main()