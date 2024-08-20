"""
Write a python program to calculate the area of the circle

radius--> take input from the user
value of pi= 3.14
output--> float, name-->area

logic-->
formula= math.pi * math.pow(r,2)
area= math.pi * math.pow(r,2)

print("area of the cirle is ",area)

Float
print(f"area of the circle is {area:2f}")

"""
import math
Radius=int(input("enter the radius:"))
print(Radius)

area= math.pi * math.pow(Radius,2)
print("area of the cirle is ", area)
print(f"area of the circle is {area:2f}")

#or can be written in one line


print(3.14*(float(input("enter the radius\n"))**2))