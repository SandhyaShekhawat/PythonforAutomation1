# Program to find maximum bw three numbers.

"""
Logic:

1. user input---> integer

2. output--> integer

3. logic if elif

if number3>number1 and number3>number2
elif number2>number1 and number2>number3
and else

"""

number1 = int(input(" enter number1:\n"))
number2 = int(input(" enter number2:\n"))
number3 = int(input(" enter number3:\n"))

if number3 > number1 and number3 > number2:
    print(f"maximum number is: {number3}")
elif number2 > number1 and number2 > number3:
    print(f"maximum number is: {number2}")

else:
    print(f"maximum number is {number1}")
