import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def user_speech():
    global speech
  
    try:
        speech = str(input("Paste your speech below:\n"))
    except:
        print("ERROR: INVALID INPUT\n")
        user_speech()

    clear()
    speech_length_calculator()


def speech_length_calculator():
    word_count = len(speech.split())

    speed = 0.4 #seconds per word based on an average talking speed of 150 words per minute

    total_seconds = int(word_count * speed)

    total_minutes = int(total_seconds / 60)
    leftover_seconds = (total_seconds - (total_minutes*60))

    if total_minutes == 1:
        print("Speech Length:\n{} minute and {} seconds\n".format(total_minutes, leftover_seconds))
    else:
        print("Speech Length:\n{} minutes and {} seconds\n".format(total_minutes, leftover_seconds))


clear()
user_speech()