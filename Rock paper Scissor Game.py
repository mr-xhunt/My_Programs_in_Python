print("This is rock paper scissor game (developed by:- Mayank Kumar Choubey)\n\n")

import random
import math
num_of_game = 0
win = 0
lose = 0 
tie = 0

def userInput(numinp):
    # Devine local variable
    newnum = math.nan
    
    # checking validity of input == number
    while True:
        num = input(numinp)
        try:
            # typecasts the input into Integer
            float(num)
        except ValueError:
            # error handling if input =/ number
            print("Error: Invalid Num")
        else:
            # Typecasting
            newnum = int(num)
            break
    return newnum

while True:
    
    lst = ["rock", "paper", "scissor"]
    choice = random.choice(lst)

    print("Press 1 for rock\n")
    print("Press 2 for paper\n")
    print("Press 3 for scissor\n")

    usr_input = userInput("Enter your Choice: ")

    if usr_input == 1 and choice == "rock":
        print(choice, "This is a Tie!\n")
        tie = tie + 1
    elif usr_input == 2 and choice == "paper":
        print(choice, "This is a Tie!\n")
        tie = tie + 1
    elif usr_input == 3 and choice == "scissor":
        print(choice, "This is a Tie!\n")
        tie = tie + 1
    elif usr_input == 1 and choice == "paper":
        print(choice, "Oops you lost the game\n")
        lose = lose + 1
    elif usr_input == 2 and choice == "scissor":
        print(choice, "Oops you lost the game\n")
        lose = lose + 1
    elif usr_input == 3 and choice == "rock":
        print(choice, "Oops you lost the game\n")
        lose = lose + 1
    elif usr_input > int(3) or usr_input < int(1):
        print("Enter valid choice\n")
    else:
        print(choice, "Huray! you won the game\n")
        win = win + 1
    
    num_of_game = num_of_game + 1
    if num_of_game == 5:
        print("Game Over\n")
        print("You won  ", win, " matches")
        print("You lost ", lose, " matches")
        print(tie, " matches tied")
        break


