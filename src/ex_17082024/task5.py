# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

number1=float(input("enter the first number"))
number2=float(input("enter the second number"))

if (number1>number2):
    print("number1 is greater than number2")
elif (number1<number2):
    print("number1 is less than number2")
else:
    print("number1 is equal to number2")

#or

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
        print(f"{num1} is less than {num2}")
else:
        print(f"{num1} is equal to {num2}")

