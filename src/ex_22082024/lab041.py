"""

#match statement


Write a program to ask the user which browser he wants to run automation.

"""

browser_name = input("Enter the browser name:\n")

match browser_name:
    case "chrome":
        print("execute the chrome code")
    case "firefox":
        print("execute the firefox code")
    case "edge":
        print("execute the edge code")
    case "safari":
        print("execute the edge code")
