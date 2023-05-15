import os
import base64


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_selection():
    selection = input("Would you like to encode (E) or decode (D) a message?\n").upper()

    if selection == "E":
        clear()
        encoder()
    elif selection == "D":
        clear()
        decoder()
    else:
        print("ERROR: INVALID SELECTION\n")
        user_selection()


def encoder():
    message = str(input("Paste your message below:\n"))
    
    clear()

    encoded_message = base64.urlsafe_b64encode("".join(message).encode()).decode()
    print("Encoded Message:\n{}\n".format(encoded_message))


def decoder():
    encoded_message = str(input("Paste your encoded message below:\n"))

    clear()

    decoded_message = base64.urlsafe_b64decode(encoded_message).decode()
    print("Decoded Message:\n{}\n".format(decoded_message))


clear()
user_selection()