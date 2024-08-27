# fabonacci series
# 0 1 1 2 3 5 8
# 0 0+1 1+1 2+1 3+2 5+3
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1

print("fabonacci series")
count = 0
while count <= num_terms:
    print(a, end=' ')

    a, b = b, a + b
    count = count + 1

"""
   a,b=0,1
   a,b=1,1
   a,b=1,2
   a,b=2,3
   a,b=3,5
   a,b=5,8
   a,b=8,13
"""
