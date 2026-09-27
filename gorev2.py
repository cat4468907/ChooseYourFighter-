def CYF():
    fighter = input("choose your fighter! (type CMF to view options): ")
    
    if fighter == "CMF":
        print("Saitama/Goku/Naruto")
    else:
        print("Please type CMF")

CYF()

def CYF2():
    fighter = input("its time to choose!): ")
    
    if fighter == "CMF":
        print("Saitama/Goku/Naruto")
    elif fighter == "Goku":
        print("Good Choice!")
    elif fighter == "Saitama":
        print("Kinda good :>")
    elif fighter == "Naruto":
        print("holy moly...")
    elif fighter == "Kitten":
        print("Congrats! You unlocked an easter egg!")
    else:
        print("Coming Soon!")

CYF2()



def EYA():
    age = int(input("Enter Your Age!: "))
    
    if age < 18:
        print("i dont believe in you but you still can try!, go on!")
    elif age > 18:
        print("Go on! i believe in you!")
    else:
        print("okie!")

EYA()