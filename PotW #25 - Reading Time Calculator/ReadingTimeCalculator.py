import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def book_length():
    global pages
  
    try:
        pages = int(input("Enter the number of pages in the book:\n"))
    except:
        print("ERROR: INVALID INPUT\n")
        book_length()

    clear()
    page_length()


def page_length():
    global words_per_page
    
    try:
        words_per_page = int(input("Enter an estimate for the average number of words per page:\n"))
    except:
        print("ERROR: INVALID INPUT\n")
        page_length()
    
    clear()
    book_reading_time_calculator()


def book_reading_time_calculator():
    word_count = pages * words_per_page

    speed = 250 #words per minute

    total_minutes = int(word_count / speed)

    total_hours = int(total_minutes / 60)

    if total_hours == 0:
      leftover_minutes = total_minutes
    else:
      leftover_minutes = int(total_minutes - (total_hours*60))

    if total_hours == 0 and leftover_minutes == 1:
        print("Time to read a {}-page book that has an average of {} words per page:\n{} minute\n".format(pages, words_per_page, leftover_minutes))
    elif total_hours == 0:
        print("Time to read a {}-page book that has an average of {} words per page:\n{} minutes\n".format(pages, words_per_page, leftover_minutes))
    elif total_hours == 1:
        print("Time to read a {}-page book that has an average of {} words per page:\n{} hour and {} minutes\n".format(pages, words_per_page, total_hours, leftover_minutes))
    else:
        print("Time to read a {}-page book that has an average of {} words per page:\n{} hours and {} minutes\n".format(pages, words_per_page, total_hours, leftover_minutes))


clear()
book_length()