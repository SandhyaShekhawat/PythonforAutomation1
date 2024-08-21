"""
Grade Calculator:

Write a program that calculates and display letter grade for the given numerical score.

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F:0-59

"""

user_score=float(input("Enter your marks scored:\n"))
print(user_score)

if 90 <= user_score <= 100:
    grade="A"
    print(f"Your grade is: {grade}")
elif 80 <= user_score <= 89:
    grade="B"
    print(f"Your grade is {grade}")
elif 70 <= user_score <= 79:
    grade="C"
    print(f"Your grade is {grade}")
elif 60 <= user_score <= 69:
    grade="D"
    print(f"Your grade is {grade}")
elif user_score>100:
    print("Not a valid input,exceeds the maximum score")
else:
    grade="F"
    print(f"Your grade is {grade}")
