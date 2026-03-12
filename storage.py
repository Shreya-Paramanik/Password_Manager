from encryption import *
from utils import *
import json
import os

FILE_NAME = "vault.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r") as f:
        stored_credentials = json.load(f)
else:
    stored_credentials = {}




def save_data():
    with open(FILE_NAME,"w") as f:
        json.dump(stored_credentials,f,indent=4)



def addNew():
    website = input(str("Website :"))
    username = input(str("Username :")).strip()
    user_consent = input(str("1. Enter Password Manually, 2. Generate secure password"))

    if(user_consent == "2"):
        password = Generate_Pass()
        print(password)
    else:
        password = input(str("Password(Ensure it contains both letters and numbers):")).strip()

   
    

    # print(username,username.isalpha())
    # print(password.isalnum())

    if((username.isalnum() or username.isalpha()) and password.isalnum()):
        passwd = encrypt(password)
        
        stored_credentials[website] = {
            "username":username,
            "password":passwd.decode()}
        
        save_data()
        print("Succesfully Stored")



    else:
        print("Please ensure USERNAME is Alphabetic and PASSWORD is Alpha numeric")

        

def retrieveCred():
    website = input(str("Enter website :"))
    data = stored_credentials.get(website,None)
    print(data["password"])
    password = data["password"]
    if(password):
        decrypted_pass = decrypt(password)

        print(f"Website : {website}")
        print(f"Username : {data["username"]}")
        print(f"Password : {decrypted_pass}")
        print()
    else:
        print("No website like this is stored")   

    



def updateCred():
    website = input(str("Enter Website :"))
    data = stored_credentials.get(website,None)

    if(data):
        print(f"OLD PASSWORD : {decrypt(data["password"])}")
        new_pass = input(str("Enter new password :"))
        confirm_pass = input(str("Enter your new password again: "))

        if(new_pass == confirm_pass):
           encrypted_passwd =  encrypt(new_pass)

           stored_credentials[website] = {
                "username":data["username"],
                "password": encrypted_passwd.decode()}

           save_data()
          
           print("Successfully Updated Password")   



def deleteCred():
    website = input(str("Enter Website :"))
    data = stored_credentials.pop(website,None)

    if(data == None):
        print("Key Not Found")
    else:
        print("Successfully deleted")


def listAll():
    for value in stored_credentials:
        username = stored_credentials[value]["username"]
        passwd = stored_credentials[value]["password"]

        decrypted_passwd = decrypt(passwd)

        print(f"Website : {value}")
        print(f"Username: {username}")
        print(f"Password : {decrypted_passwd}")
        print()