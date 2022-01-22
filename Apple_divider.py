import math
def userInput(numinp):
    # Devine local variable
    newnum = math.nan
    
    # checking validity of input == number
    while True:
        num = input(numinp)
        try:
            # typecasts the input into int
            int(num)
        except ValueError:
            # error handling if input =/ number
            print("Error: Invalid Num")
        else:
            # Typecasting
            newnum = int(num)
            break
    return newnum
while True:
    n = userInput("Enter the no. of Apples you have:  ")
    print("Enter the range:\n")
    mn = userInput("Start range: ")
    mx = userInput("End range: ")
    my = mx + 1
    if mn>mx:
        print("First number should always be smaller than second no. in a Range!")
        break
    if mn == mx:
        print("Range Cannot be equal!")
        for num in range(mn,my):
            if num == 0:
                print("Apples cannot be divided by zero")
            elif n%num == 0:
                print(f"{num} is divisor of {n}")
            else:
                print(f"{num} is not a divisor of {n}")
    else:
        for num in range(mn,my):
            if num == 0:
                print("Apples cannot be divided by zero")
            elif n%num == 0:
                print(f"{num} is divisor of {n}")
            else:
                print(f"{num} is not a divisor of {n}")
        