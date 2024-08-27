#can call one function in another function.

def greet():
    print("Goodmorning, Everyone")

def name():
    greet()
    print("What is your name:")
name()


"""
O/p when only name() function is called

Goodmorning, Everyone
What is your name:

as we called the greet function in name function also, and it is now also part of name function.

we acn call the greet() func seperately also.
"""