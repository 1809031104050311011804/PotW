import os


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def supported_courses():
    print("This program currently supports the following courses:\n\n(1) Augusta National Golf Club\n(2) TPC Scottsdale\n(3) Pebble Beach Golf Links\n")
    
    global hole_numbers

    hole_numbers = list(range(1,19))

    #(1) Augusta National Golf Club
    global augusta_pars, augusta_yardages
    
    augusta_pars = [4, 5, 4, 3, 4, 3, 4, 5, 4,
                    4, 4, 3, 5, 4, 5, 3, 4, 4]
    augusta_yardages = [445, 575, 350, 240, 495, 180, 450, 570, 460,
                        495, 505, 155, 510, 440, 530, 170, 440, 465]
    
    #(2) TPC Scottsdale
    global scottsdale_pars, scottsdale_yardages
    
    scottsdale_pars = [4, 4, 5, 3, 4, 4, 3, 4, 4,
                       4, 4, 3, 5, 4, 5, 3, 4, 4]
    scottsdale_yardages = [403, 442, 558, 183, 470, 432, 215, 475, 453,
                           428, 472, 192, 558, 490, 553, 163, 332, 442]

    #(3) Pebble Beach Golf Links
    global pebble_beach_pars, pebble_beach_yardages
    
    pebble_beach_pars = [4, 5, 4, 4, 3, 5, 3, 4, 4,
                         4, 4, 3, 4, 5, 4, 4, 3, 5]
    pebble_beach_yardages = [378, 509, 397, 333, 189, 498, 107, 416, 483,
                             444, 370, 202, 401, 559, 393, 400, 182, 541]

    user_course()


def user_course():
    global course, course_name, pars, yardages
  
    try:
        course = int(input("Which course would you like to see the yardage book for (#)?\n"))
        
        if course == 1:
            course_name = "Augusta National Golf Club"
            pars = augusta_pars
            yardages = augusta_yardages
            clear()      
            course_hole()
        elif course == 2:
            course_name = "TPC Scottsdale"
            pars = scottsdale_pars
            yardages = scottsdale_yardages
            clear()      
            course_hole()
        elif course == 3:
            course_name = "Pebble Beach Golf Links"
            pars = pebble_beach_pars
            yardages = pebble_beach_yardages
            clear()      
            course_hole()
        else:
            print("ERROR: COURSE NOT SUPPORTED\n")
            user_course()

    except:
        print("ERROR: INVALID INPUT\n")
        user_course()


def course_hole():
    global hole
    
    try:
        hole = int(input("Which hole would you like to see the yardage for (#)?\n"))
        hole = hole - 1
    except:
        print("ERROR: INVALID INPUT\n")
        course_hole()

    if hole >= 0 and hole <= 17:
        hole_yardage()
    else:
        print("ERROR: HOLE NUMBER OUTSIDE OF RANGE\n")
        course_hole()


def hole_yardage():
    clear()
    print("{}\n\bHole #{}\nPar {}\n{} Yards\n".format(course_name, hole_numbers[hole], pars[hole], yardages[hole]))


clear()
supported_courses()
