"""
Loops:
A block of code that we want to repeat and execute multiple times.
There are two types of loops in python:
For loop
while loop
"""
"""
for loop:

Syntax:
 for variable_name in the range(start,stop,step)
"""
for i in range(1,10):
    print(i)
"""
range(): 

class range(Sequence[int])

range(stop) -> range object range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. 
range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. 
These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).
"""
# For printing even numbers b/w 2 and 11, specifying step as 2:
for i in range(2,11,2):
    print(i)


