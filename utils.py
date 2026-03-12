import random
import string

def Generate_Pass():
    chars = string.ascii_letters + string.digits 

    password = ''.join(random.choice(chars)for _ in range(16))

    return password
   
