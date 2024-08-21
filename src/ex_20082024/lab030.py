# write a program to find max b/w two numbers.
"""
steps:
1. input is taken from the user
write input statements---> will take two integers

2.Output:
Maximum out of two

3. Logic:
use if else
or max function
"""

num1=int(input("Enter num1:\n"))
print(num1)
num2=int(input("Enter num2:\n"))
print(num2)

print("the maximum number is: ", max(num1,num2))

#OR

number1=int(input("enter number1:\n"))
number2=int(input("enter number2:\n"))

if number1>number2:
    print(f"The maximum number is: {number1}")

else:
    print(f"the maximum number is: {number2}")



