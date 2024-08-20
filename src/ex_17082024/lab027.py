"""

Ternary operators:

Works with conditions
this or that
"""

print( "I will go to goa" if int(input("enter your age"))>18 else"I will not go to goa")

# Or you can write the sae code in multiple lines

userage= int(input("enter your age"))
if userage>18:
    print("I will go to goa")
else:
    print("I will not go to goa")