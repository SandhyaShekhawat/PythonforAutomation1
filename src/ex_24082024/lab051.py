#Arguments with return type:


def sum_of_two_numbers(num1=40,num2=50):
    return num1+num2

result=sum_of_two_numbers(10,20)

print(result)

result2=sum_of_two_numbers(num2=30,num1=20)
print(result2)


result3=sum_of_two_numbers(num2=30)
print(result3)

result4=sum_of_two_numbers()
print(result4)
"""
O/p
30
50
70
90

"""