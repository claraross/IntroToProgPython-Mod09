# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <Your Name>,<Today's Date>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

from ProcessingClasses import FileProcessor as FileProcessor
from IOClasses import EmployeeIO


# Main Body of Script  ---------------------------------------------------- #

# exceptions
class InvalidChoice(Exception):
    def __str__(self):
        return "Please choose from menu: option 1, 2, 3, or 4."


# initialize variables
strFileName = "EmployeeData.txt"

# Load data from file into a list of employee objects when script starts
lstEmployees = FileProcessor.read_data_from_file(strFileName)
EmployeeIO.print_current_list_items(lstEmployees)
# Show user a menu of options
while True:
    try:
        EmployeeIO.print_menu_items()
        intUserChoice = int(EmployeeIO.input_menu_options())
        if intUserChoice == 1:
            EmployeeIO.print_current_list_items(lstEmployees)
        elif intUserChoice == 2:
            newEmployee = EmployeeIO.input_employee_data()
            lstEmployees.append(newEmployee)
        elif intUserChoice == 3:
            FileProcessor.save_data_to_file(strFileName, lstEmployees)
        elif intUserChoice == 4:
            break
        else:
            raise InvalidChoice()
    except ValueError as e:
        print("Please choose number from options above!")
    except Exception as e:
        print("There was an error. The built in message from Python is:")
        print(e)
