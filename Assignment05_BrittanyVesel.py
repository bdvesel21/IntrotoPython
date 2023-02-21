# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Brittany Vesel, February 19, 2023, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
constStrKey_Task = "Task"
constStrKey_Priority = "Priority"


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {constStrKey_Task: lstRow[0], constStrKey_Priority: lstRow[1].strip()}
    lstTable.append(dicRow)
#    print(dicRow[constStrKey_Task] + " ~ " + dicRow[constStrKey_Priority]) #Using for debug to see original data
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your current data is: ")
        print(constStrKey_Task, constStrKey_Priority, sep="\t")
        for row in lstTable:
            print(row[constStrKey_Task], row[constStrKey_Priority], sep="\t")
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a Task: ")
        strPriority = input("Enter a Priority: ")
        dicRow = {constStrKey_Task:strTask, constStrKey_Priority:strPriority}
        lstTable.append(dicRow)
#        for row in lstTable:
#            print(row[constStrKey_Task], row[constStrKey_Priority], sep="\t") #Used to debug and see results
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("What task do you want to remove?: ")
        rowFound = False
        keepSearching = True
        while(keepSearching):
            keepSearching = False
            for dicRow in lstTable:
                if dicRow["Task"].lower() == strTask.lower():
                    lstTable.remove(dicRow)
                    print("\nOkay, I deleted", strTask, "and it had priority: ", dicRow[constStrKey_Priority])
                    rowFound = True
                    keepSearching = True
                    break
            continue
        if (rowFound == False):
            print(strTask, "was not found!")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Would you like to Save your Data?")
        strChoice2 = str(input("Enter 'y' or 'n': "))
        if strChoice2.lower() == 'y':
            objFile = open("ToDoToDoList.txt", "w")
            for row in lstTable:
                objFile.write(row[constStrKey_Task] + "," + row[constStrKey_Priority] + "\n")
            objFile.close()
            print("Data was saved!")
        else:
            print("Data not saved! Returning to menu...")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting...")
        break  # and Exit the program
