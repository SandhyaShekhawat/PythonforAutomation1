"""
user defined functions:

def great()

Function's name be only numbers and special characters.
"""
"""
Example1: This will give you: SyntaxError: invalid syntax
def 123():
    print("hello")

123()
"""


# Example2: underscore as a function name is acceptable:
def _():
    print(" hello world ")


_()


# Example 3: combination of letters and numbers: valid name:  o/p-->Hi I am Sandhya

def sandhya123():
    print(" Hi I am Sandhya ")


sandhya123()


# Example4:

def sandhya_():
    print("hi")


sandhya_()

#Example5: cannot use camel case:

def camelCase():
    print("Hello")

camelCase()
