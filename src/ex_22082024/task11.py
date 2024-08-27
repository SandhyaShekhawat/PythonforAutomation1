# fabonacci series
# 0 1 1 2 3 5 8
# 0 0+1 1+1 2+1 3+2 5+3
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1

print("fabonacci series")
i = 0
while i <= num_terms:
    print(a, end=' ')
    a, b = b, a + b
    i = i+1
