import pandas as pd
import os

def file():
    global file_path, file_name, file_extension, data
    file_path = input("\nWhat is the file path for your data (i.e., Documents/Data)?\n")
    file_name = input("\nWhat is the file name of your data?\n")
    file_extension = input("\nWhat is the file extension of your data? Note: this program currently only supports Microsoft Excel files.\n")

    try:
        data = pd.read_excel(os.path.join(file_path, "{}.{}".format(file_name,file_extension)))
    except:
        print("Your file could not be found.")
        re_enter_choice()
    else:
        data_load()
                
def re_enter_choice():
    choice1 = input("\nWould you like to re-nter your file information (Y/N)?\n")
    if choice1 == "Y":
        file()
    elif choice1 == "N":
        exit()
    else:
        print("Please answer Y/N.")
        re_enter_choice()

def data_load():
    print("\nLoading data...\n")
    print(data)
    data_choice()
    
def data_choice():
    choice2 = str(input("\nWould you like to analyze your data (Y/N)?\n"))
    if choice2 == "Y":
        data_analyzer()
    elif choice2 == "N":
        exit()
    else:
        print("Please answer Y/N.")
        data_choice()

def data_analyzer():
    numeric_columns = numeric_columns = data.dtypes[data.dtypes=="int64"].index.values.tolist()
    
    print("\nThis program currently supports the following types of data analysis:\nOption #1: Minimum, Maximum\nOption #2: Mean, Standard Deviation\nOption #3: Minimum, Maximum, Mean, Standard Deviation")
    try:
        choice3 = int(input("\nWhich option would you like to use?\n"))
    except:
        print("Please enter a valid option #.")
        data_analyzer()

    column_choice = input("\nWhich column would you like to analyze? Your available columns are {}.\n".format(numeric_columns))

    if choice3 == 1:
        try:
            option1 = data.agg({column_choice: ["min", "max"]})
            print(option1)
        except:
            print("No data analysis was performed.")
    elif choice3 == 2:
        try:
            option2 = data.agg({column_choice: ["mean", "std"]})
            print(option2)
        except:
            print("No data analysis was performed.")
    elif choice3 == 3:
        try:
            option3 = data.agg({column_choice: ["min", "max", "mean", "std"]})
            print(option3)
        except:
            print("No data analysis was performed.")
    else:
        print("No data analysis was performed.")

file()
