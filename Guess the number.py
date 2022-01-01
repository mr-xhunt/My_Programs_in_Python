"""This Program is developed by Mayank Kumar Choubey
and Thanks a lot to Code With Harry for teaching Python in most easy way! """


import random
import math
n = random.randint(1,100)
# print(n)
i = 0

def userInput(numinp):
    # Devine local variable
    newnum = math.nan

    # Checking Validity of input == number
    while True:
        num = input(numinp)
        try:
            # typecasts the input into integer
            int(num)
        except ValueError:
            # error handling if input =/ number
            print("Error: Invalid Num")
        else:
            # Typecasting
            newnum = int(num)
            break
    return newnum

while(True):
    numinp = userInput("\nGuess the number:\n\n")
    if numinp==n:
        print(numinp, "Hurray you guessed the number right\n")
        print(f"You took {i} turn to win the Game!")
        break
    elif numinp<n:
        print(numinp, "It is lesser than the required number\n")
    elif numinp>n:
        print(numinp, "It is greater than the required number\n")
    else:
        print("INVALID NUMBER\n")
    if(i==10):
        print("Game over\n\n")
        break

    i = i + 1
    print("Guesses left", 10-i)
