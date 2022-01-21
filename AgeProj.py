import math

class Age:    
    def Age_in_2090(self):
        age_dob = input ("Enter your age or dob:  ")
        try:
            int(age_dob)
        except Exception:
            print("This is not a valid argument!")
        else:
            age_dob = int(age_dob)
            name = input ("Enter your name:  ")
            if age_dob < 100 and age_dob > 0:
                age = 68 + age_dob
                print(f"{name} You will be {age} years old in 2090")
            elif age_dob > 1950 and age_dob <2022:
                age = 2022-age_dob
                print(f"{name} You will be {age} years old in 2090")
            elif age_dob >2022:
                print("Looks like you are from the future")
            elif age_dob <1950 or age_dob>100:
                print("Looks like you are the oldest person alive")

    def Age_when_100(self):
        age_dob = input ("Enter your age or dob:  ")
        try:
            int(age_dob)
        except Exception:
            print("This is not a valid argument!")
            
        else:
            age_dob = int(age_dob)
            name = input ("Enter your name:  ")
            if age_dob<100 and age_dob>0:
                when_100 = (100-age_dob) + 2022
                print(f"{name} you will be 100 years old in {when_100}") 
            if age_dob>1921 and age_dob<2023:
                when_100 = 2022 - age_dob
                print(f"{name} you will be 100 years old in {when_100}")
            else:
                print("You are not a valid person to be here!")

age = Age()
while True:
    print("Type 'Q' or 'q' to quit\n")
    choice = input("What do you want to do?\n 1. Age in 2090\n 2. Age when 100\n\n Press 1 or 2...  ")
    if choice == "Q" or choice == "q":
        break
    elif int(choice) == 1:
        age.Age_in_2090()
    elif int(choice) == 2:
        age.Age_when_100()
    else:
        print("Enter a valid choice!")



