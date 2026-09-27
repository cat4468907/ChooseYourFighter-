def psswdcheck():
    psswd = input("choose a password: ")
    
    if psswd == "mydick":
        print("password too short!")
    elif psswd == "yourdick":
        print("password too long!")
    else:
        print("password created succesfully!")

psswdcheck()
