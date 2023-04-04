import os
import random
import time


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


#https://www.rd.com/list/funniest-one-liners-you-havent-heard-yet/
puns = ["Did you hear they arrested the devil?",                        "Yeah, they got him on possession.",
        "What did one DNA say to the other DNA?",                       "Do these genes make me look fat?",
        "My IQ test results came back.",                                "They were negative.",
        "What do you get when you cross a polar bear with a seal?",     "A polar bear.",
        "Why can't you trust an atom?",                                 "Because they make up literally everything.",
        "What’s the difference between an outlaw and an in-law?",       "Outlaws are wanted.",
        "What happens to an illegally parked frog?",                    "It gets toad away.",
        "How does the man in the moon get his hair cut?",               "Eclipse it.",
        "What do you call a bear with no teeth?",                       "A gummy bear.",
        "What do you call a mobster who’s buried in cement?",           "A hardened criminal.",
        "What do fish say when they hit a concrete wall?",              "Dam!",
        "Give a man a fish, and he will eat for a day.",                "Teach a man to fish, and he will sit in a boat and drink beer all day.",
        "Why don’t pirates take a shower before they walk the plank?",  "They just wash up on shore.",
        "How much did Santa pay for his sleigh?",                       "Nothing, it was on the house.",
        "What do you call a steak that’s been knighted by the queen?",  "Sir Loin.",
        "Why didn’t Han Solo enjoy his steak dinner?",                  "It was Chewie.",
        "Why did the rooster cross the road?",                          "To prove he wasn’t a chicken.",
        "What did the zookeeper say after the python broke free?",      "Nothing.",
        "Why don’t cats play poker in the jungle?",                     "Too many cheetahs.",
        "What do you call a guy who’s had too much to drink?",          "A cab.",                                                                   ]


def random_pun_choice():
    global pun_number
    
    pun_number = random.randrange(0, len(puns), 2)

    random_pun_set_up()


def random_pun_set_up():
    print(puns[pun_number])

    time.sleep(3)

    random_pun_punchline()


def random_pun_punchline():
    print("")
    print(puns[pun_number+1])
    print("")


clear()
random_pun_choice()