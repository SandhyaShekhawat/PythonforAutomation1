"""
character literals:

single character enclosed in single quotation marks
Escape sequence
ASCII value
UNICODE Character
Octal character
"""

"""
Escape sequence:



"""

print("hello world")

print("hello/nworld")   # new line

print("hello/bworld")   # backspace

print("hello/tworld")   # tab space

"""
r concept
where to use r concept?
It is used in automation.
when storing file paths
for storing the file path--> use r and see the difference, r here means raw.
"""

#print("C:\sandhya\n.txt")
print(r"C:\sandhya\n.txt")


"""
If one needs to right names with a single or double quotes
it is same as writing the sting in case of double quotes but for single quotes we need to use escape sequence
   "\"
Lets see with the example below

"""

name="sandhya's"
print(name)
#name='sandhya's' ---> will show unterminated string literal Syntaxerror

name='sandhya\'s' #use backslash

print(name)



