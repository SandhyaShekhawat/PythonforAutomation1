#How to take user input?

Name= input("Write your name here:")

print(Name)

#to know the datatype use type function
#type()

print(type(Name))

#The datatype of input taken using input() function will always be string

"""

we are unable to perform mathematical operation on these numbers as they are string datatype.
addition of the two will lead to concatination of strings.

Ex:
num1=(input("enter the first number"))-->23
num2=int(input("enter the second number"))-->34
print(num1+num2) ---> 2334

In order to perform mathematical operation, we need to convert them into Integer
to convert it into another datatype and use it for further operation.

"""

num1=int(input("enter the first number"))
print(type(num1))

num2=int(input("enter the second number"))
print(type(num2))

print(num1+num2)

"""
Python is very smart language
it gives the division operation result in float
since in most cases division results in float value

Ex:
"""

print(num1/num2)    #45/45--->1.0