def sifrekontrol():
    sifre = input("choose a password: ")
    
    if sifre == "mydick":
        print("password too short!")
    elif sifre == "yourdick":
        print("password too long!")
    else:
        print("password created succesfully!")

sifrekontrol()
