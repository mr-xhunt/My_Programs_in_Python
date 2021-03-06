"""
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222

"""
print("This program gives immediate next Palindrome no. to your given numbers.\n")
entries = input("Input no. of entries you like to give: ")
try:
    int(entries)
except:
    print("Invalid no.!")
else:
    int_ent = int(entries)
    for i in range(int_ent):
        num = input(f"Enter your {i+1} number: ")
        try:
            int(num)
        except:
            print("Invalid No.!")
        else:
            new_num = int(num)
            new_num2 = new_num
            while True:
                new_num += 1 
                str_num = str(new_num)
                if str_num == str_num[::-1]:
                    print(f"The Immediate next Palindrome of {new_num2} is {str_num}")
                    break
                else:
                    continue