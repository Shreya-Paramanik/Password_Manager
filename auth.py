def login():
    MASTER_USERNAME = "SHREYA"
    MASTER_PASSWORD = "SHREYA2005"

    username = input(str("ENTER USERNAME:"))
    password = input(str("ENTER PASSWORD:"))

    if(username == MASTER_USERNAME and password == MASTER_PASSWORD):
        return True
    else:
        return False
