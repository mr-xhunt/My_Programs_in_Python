# make a program
# take input of lists
# output:
# print three list : one will be reversed of the given input , second will be swaped by like first thing to last second to second last and so on,
#  third by using one of a built in function


food_calories=list(input("Enter The Calories:").split(","))
print(food_calories)

l2=list(reversed(food_calories))
l3=food_calories[::-1]

length=len(food_calories)

for i in range(length//2):
    temp=food_calories[i]
    food_calories[i]=food_calories[-1+-i]
    food_calories[-i+-1]=temp
print(l2)
print(l2)
print(food_calories)
if(l2==l3==food_calories):
    print("Same")






