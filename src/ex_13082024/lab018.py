#"str" datatype:

name="Sandhya"

print(type(name))
print(name.upper())
print(name.lower())

# cannot use len() function like this--->print(name.len())

"""
can we add integer to a string


name1="sam"
name1= name1+ 1           #---> this will show error


name1= name1+ 1           #---> this will show error
           ~~~~~^~~
TypeError: can only concatenate str (not "int") to str

"""

#we can use it by quoting -->concatination

name1="sam"
name1=name1 + "1"
print(name1)             #---> O/P : sam1

#        OR

name1=name1 + str(2)
print(name1)            #---> sam12





