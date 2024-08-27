
number=int(input("Enter the number:\n"))
factorial=1
for i in range(1, number + 1):
    factorial = factorial * i
    """
    factorial=1*1 -->1
    factorial=1*2-->2
    factorial=2*3-->6
    factorial=6*4-->24
    factorial=24*5-->120

    factorial=120

     """
print("factorial of the given number is", factorial)