#always use comparison operator in conditions because it returns value true or false.
#use "==" and not the assignment operator "="
#Program

a=8

if a==10:         # need to ue the comparison operator == returns the value false in this case and hence else condition is executed
    print("Hello worls")

else:
    print("Hi")

"""
cannot write the above program as:

a=8

if a=10:     ----------> this will throw error: SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
     print("hello world)

else:
    print("hi")




"""

