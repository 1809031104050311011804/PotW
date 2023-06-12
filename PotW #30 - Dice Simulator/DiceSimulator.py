#The bulk of this code is sourced from:
#https://pythongeeks.org/python-dice-rolling-simulator/


import os
import tkinter
from PIL import Image, ImageTk
import random


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


root = tkinter.Tk()
root.geometry("200x200")
root.title("Dice Simulator")

dice =  [os.path.join(os.path.dirname(__file__), "Dice", "1.png"),
         os.path.join(os.path.dirname(__file__), "Dice", "2.png"),
         os.path.join(os.path.dirname(__file__), "Dice", "3.png"),
         os.path.join(os.path.dirname(__file__), "Dice", "4.png"),
         os.path.join(os.path.dirname(__file__), "Dice", "5.png"),
         os.path.join(os.path.dirname(__file__), "Dice", "6.png")]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label1.image = image1
label1.pack(expand=True)


def rolling_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1


button=tkinter.Button(root,text="Click to roll the die!",fg="black",command=rolling_dice)
button.pack(expand="True")


clear()
root.mainloop()