"""
Conditions and loops:

ifelse loop:

syntax:
if condition
// code u want to execute if the condition is true

else condition
// code u want to execute if the condition is false

"""

#Program: write a program that takes user age as input and let the user know if he/she can go to club?


user_age=int(input("Enter your age:\n"))

print(user_age)

if user_age>=21:
    print("You can go to the club")

else:
    print("You cannot go to the club")
