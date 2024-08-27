"""
 *args:

 This is used for multiple args, any no. of arguments can be passed.

"""

def greet( *args ):
    print(args[0])
greet("sandhya","Bhavya","Himmat")
greet("Bhavya","Himmat")
greet("Bhavya","Himmat")
greet(10,"Bhavya","Himmat")
greet(20,10,"Bhavya","Himmat")
greet(40,True,"Bhavya","Himmat")
greet("Himmat")


"""
O/P:
sandhya
Bhavya
Bhavya
10
20
40
Himmat
IndexError: tuple index out of range---> if greet()
Print() also takes multiple args.
"""

"""
For printing everything from the list

"""

def greetings(*args):
    for i in args:
        print(i)

greetings(10,20,40,3.14,True,False,"sandhya","Himmat")
