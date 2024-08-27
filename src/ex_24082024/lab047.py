# Functions with arguments and parameters.

def greet():
    print("Goodmorning, Everyone")

def name(name):

    print("What is your name:", name)


name("Himmat")

"""
For calling name function now we will need to satisfy name argument condition also,
otherwise, code will give an error.

Error:
TypeError: name() missing 1 required positional argument: 'name'


name("Himmat")

name(123)
name(3.14)
"""
"""
Also we can take input for name from the user

def name(name):

    print("What is your name:", name)
name=input("Enter your name:"\n)

o/p
Enter your name:
Himmat
What is your name: Himmat

"""