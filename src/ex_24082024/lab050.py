#No return type with default argument.

def greet(name="sandhya"):
    print("Hello", name.upper())

result= greet("Bhavya")
print(result)

result2=greet()
print(result2)

"""
Output:

Hello Bhavya
None
Hello sandhya
None

.upper will print the names in capitals
Hello BHAVYA
None
Hello SANDHYA
None
"""

#with multiple args:

def multiple_args(name1,name2,name3):
    print("hi", name1, name2,name3)

result=multiple_args("sandhya","bhavya","rohit")

print(result)

"""
O/p:
hi sandhya bhavya rohit
None

"""