import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def email_slicer():
    email = input("Enter your email address:\n").strip()

    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]

    clear()

    print("Username:\n{}\n".format(username))
    print("Domain:\n{}\n".format(domain))


def main():
    clear()
    email_slicer()


main()