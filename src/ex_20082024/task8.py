"""Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
"""
side1 = int(input("Enter the first side"))
side2 = int(input("Enter the second side"))
side3 = int(input("Enter the third side"))

if side1 == side2 == side3:
    print("the triangle is equilateral triangle")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("the triangle is an isosceles triangle")

else:
    print("the triangle is scalene triangle")
