import os
import random


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


adjectives  =   ["Adorable", "Annoying",
                 "Brave", "Busy",
                 "Cautious", "Courageous",
                 "Dead", "Delightful",
                 "Eager", "Elegant",
                 "Fantastic", "Frightened",
                 "Gifted", "Grumpy",
                 "Helpless", "Hilarious",
                 "Impossible", "Inquisitive",
                 "Jealous", "Jolly",
                 "Kind", "Kingly",
                 "Lazy", "Lucky",
                 "Magnificent", "Mysterious",
                 "Nervous", "Nice",
                 "Odd", "Outstanding",
                 "Poised", "Powerful",
                 "Quaint", "Quirky",
                 "Real", "Rich",
                 "Selfish", "Sleepy",
                 "Talented", "Tough",
                 "Ugly", "Unusual",
                 "Venomous", "Versatile",
                 "Wicked", "Witty",
                 "Xenacious", "Xenial",
                 "Zany", "Zealous"              ]


nouns       =   ["Actor", "Animal",
                 "Balloon", "Brother",
                 "Cartoon", "Crowd",
                 "Death", "Doctor",
                 "Egg", "Eye",
                 "Fish", "Furniture",
                 "Garage", "Ghost",
                 "Hamburger", "Horse",
                 "Ice", "Insect",
                 "Jackal", "Juice",
                 "Kangaroo", "King",
                 "Lawyer", "Lizard",
                 "Machine", "Magician",
                 "Nail", "Napkin",
                 "Ocean", "Oyster",
                 "Pizza", "Planet",
                 "Queen", "Quill",
                 "Rain", "Rocket",
                 "Shoe", "Spoon",
                 "Teacher", "Television",
                 "Ultimatum", "Umbrella",
                 "Van", "Vulture",
                 "Whale", "Window",
                 "X-Ray", "Xylophone",
                 "Yacht", "Yak",
                 "Zebra", "Zoo"                 ]


def username_generator():
    global username

    random_adjective = adjectives[random.randint(0, len(adjectives)-1)]
    random_noun = nouns[random.randint(0, len(nouns)-1)]
    random_numbers = random.randint(0, 100000)

    username = random_adjective + random_noun + str(random_numbers)

    username_show()


def username_show():
    clear()

    print("Username:\n{}".format(username))
    print("")


username_generator()