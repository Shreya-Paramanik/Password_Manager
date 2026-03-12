from storage import *
from utils import *
from auth import *

options = {1 : "Add New Credentials",2 : "Retreive Credentials", 3 : "Update Credentials", 4 : "Delete Credentials",5 : "List all websites", 6 : "Generate Password",7 : "Exit"}



def menu():
    while True:
        for key,val in options.items():
            print(f"{key}: {val}")
        user_input = input(str("Choose a number:"))


        if user_input == "7":
            break

        elif user_input == "1":
            addNew()
        
        elif user_input == "2":
            retrieveCred()

        elif user_input == "3":
            updateCred()
            
        elif user_input == "4":
            deleteCred()

        elif user_input == "5":
            listAll()

        else:
            Generate_Pass()

        print(user_input)


if __name__ == "__main__":
    if login():
        menu()

    

    