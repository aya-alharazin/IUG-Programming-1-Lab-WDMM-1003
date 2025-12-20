'''
Exception handling is a way to handle errors gracefully
without crashing your program.
try:
    # Code that might cause an error
    risky_code()
except:
    # Code to run if ANY error occurs
    handle_error()
'''
try:
    exp = eval(input("Enter an expression "))
    print(exp)
except ZeroDivisionError:
    print("divide by zero")
except TypeError:
    print("Invalid type")

print("this is the remaining code")
