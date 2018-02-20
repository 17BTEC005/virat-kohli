import random

print("Hello! Welcome to the Rock Paper Scissors Program!")

value = False

while value == False:
    print("")
    print("Press 1 for Rock.")
    print("Press 2 for Paper.")
    print("Press 3 for Scissors.")

    UserInput = int(input("What would you like to play?"))
    UserInput2 = int(input("What would you like to play?"))
    

    if (UserInput == 1) and (UserInput2 == 1):
        value = False
        print("It's a draw; you both played Rock!")
        
    if (UserInput == 2) and (UserInput2 == 1):
        value == True
        print("You win! UserInput2 played Rock!")

    if (UserInput == 3) and (UserInput2 == 1):
        value == True
        print("You lose! UserInput2 played Rock!")
        
    if (UserInput == 1) and (UserInput2 == 2):
        value = True
        print("You lose! UserInput2 played Paper!")
        
    if (UserInput == 2) and (UserInput2 == 2):
        value == False
        print("It's a draw; UserInput2 played Paper!")

    if (UserInput == 3) and (UserInput2 == 2):
        value == True
        print("You win! UserInput2 played Paper!")
        
    if (UserInput == 1) and (UserInput2 == 3):
        value = True
        print("You win! UserInput2 played Scissors!")
        
    if (UserInput == 2) and (UserInput2 == 3):
        value == True
        print("You lose! UserInput2 played Scissors!")

    if (UserInput == 3) and (UserInput2 == 3):
        value == False
        print("It's a draw; UserInput2 played Scissors!")
