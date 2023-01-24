import os
from PIL import Image
import matplotlib.pyplot as plt


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def introduction():
    clear()
    
    print("Welcome to 8-Bit Image Converter!")
    print("This program will convert any image to an 8-bit version of itself.")

    next()


def next():
    user_continue = input("\nAre you ready to continue? (Y/N)\n").upper()

    if user_continue == "Y":
        clear()
        image()
    elif user_continue == "N":
        clear()
        exit()
    else:
        print("ERROR: INVALID INPUT")
        next()


def image():
    global file_path, image_folder, image_name, image_file_extension, image_original
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    file_path = os.getcwd()
    image_folder = input("What is the name of the folder that your image is in?\n")
    image_name = input("\nWhat is the name of the image that you would like to convert?\n")
    image_file_extension = input("\nWhat is the file extension of your image?\n")

    try:
        image_original = Image.open(os.path.join("{}/{}".format(file_path, image_folder), "{}.{}".format(image_name, image_file_extension)))
    except:
        print("ERROR: IMAGE NOT FOUND\n")
        image()

    convert_image()


def convert_image():
    global image_converted
    
    pixel_size = 8

    #https://geekyhumans.com/convert-images-to-8-bit-images-using-python/
    image_converted = image_original.resize((image_original.size[0] // pixel_size, image_original.size[1] // pixel_size), Image.NEAREST)
    image_converted = image_converted.resize((image_converted.size[0] * pixel_size, image_converted.size[1] * pixel_size), Image.NEAREST)

    show_image()


def show_image():
    clear()
    
    print("Converting image...\n")
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    plt.suptitle(image_name)

    ax1.imshow(image_original)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.set_title("Original Image")
 
    ax2.imshow(image_converted)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_title("8-Bit Image")

    plt.show()

    save_image()


def save_image():
    user_save_image = input("Would you like to save your converted image? (Y/N)\n").upper()

    if user_save_image == "Y":
        image_converted.save("{} (8-Bit Image).{}".format(image_name, image_file_extension))
        print("\nImage saved successfully to {}".format(file_path))
        convert_again()
    elif user_save_image == "N":
        convert_again()
    else:
        print("ERROR: INVALID INPUT\n")
        save_image()
    

def convert_again():
    user_convert_again = input("\nWould you like to convert another image? (Y/N)\n").upper()

    if user_convert_again == "Y":
        clear()
        image()
    elif user_convert_again == "N":
        clear()
        exit()
    else:
        print("ERROR: INVALID INPUT\n")
        convert_again()    


introduction()
