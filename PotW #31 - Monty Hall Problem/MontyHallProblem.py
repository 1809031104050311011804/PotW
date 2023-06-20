import os
import random



def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")



def create_doors():
    global doors
    
    doors = ["GOAT", "GOAT", "CAR"]
    
    print("Door #1: ???")
    print("Door #2: ???")
    print("Door #3: ???\n")
    print("Please choose a door.\n")



def shuffle_doors():
    random.shuffle(doors)



def user_choice():
    global choice_1
    
    choice_1 = int(input("Door #"))

    if choice_1 == 1 or choice_1 == 2 or choice_1 == 3:
        choice_1 -= 1
        clear()
        reveal_goat()
        stay_or_switch()
    else:
        print("ERROR: INVALID DOOR #\n")
        user_choice()
    


def reveal_goat():
    global goat_index
    
    goat_index = []
    
    for index, element in enumerate(doors):
        if element == "GOAT":
            goat_index.append(index)


    if choice_1 in goat_index:
        choice_index = goat_index.index(choice_1)

        if choice_index == 0:
            goat_index = goat_index[1]
        elif choice_index == 1:
            goat_index = goat_index[0]
    
    else:
        goat_index = goat_index[random.randint(0,1)]
    

    for d in range(len(doors)):
        if d == goat_index:
            print("Door #{}: {}".format(d+1, doors[goat_index]))
        else:
            print("Door #{}: {}".format(d+1, "???"))



def stay_or_switch():
    global choice_2

    choice_2 = str(input("\nAfter seeing where one of the goats is located, would you like to switch your original choice of Door #{}? (Y/N)\n".format(choice_1+1))).upper()

    if choice_2 == "Y":
        switch_choice()
        reveal_prize()
    elif choice_2 == "N":
        reveal_prize()



def switch_choice():
    global choice_3

    if goat_index == 0:
        if choice_1 == 1:
            choice_3 = 2
        elif choice_1 == 2:
            choice_3 = 1
    
    elif goat_index == 1:
        if choice_1 == 0:
            choice_3 = 2
        elif choice_1 == 2:
            choice_3 = 0
    
    elif goat_index == 2:
        if choice_1 == 0:
            choice_3 = 1
        elif choice_1 == 1:
            choice_3 = 0



def reveal_prize():
    clear()

    for d in range(len(doors)):
        print("Door #{}: {}".format(d+1, doors[d]))
    
    if choice_2 == "Y":
        print("\nYou decided to switch from Door #{} to Door #{}, which contained a {} behind it.".format(choice_1+1, choice_3+1, doors[choice_3]))
    elif choice_2 == "N":
        print("\nYou chose Door #{}, which contained a {} behind it.".format(choice_1+1, doors[choice_1]))

    print("")



def main():
    clear()
    create_doors()
    shuffle_doors()
    user_choice()



main()