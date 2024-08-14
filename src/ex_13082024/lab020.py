#concept--->id

#python interpretor practices best usage of memory

#Ex:

age=10
age2=10
print(id(age))
print(id(age2))

#the above two variables will return the same id value, because the value of both the variables is 10, i.e. same

age3=10
print(id(age3))
age4=20
print(id(age4))

#If I change the value of the variable

age=50
print(id(age))

#this will again give a different value of id
#memory is allocated to a variable on the basis of value
