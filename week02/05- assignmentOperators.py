'''
🟦 Assignment Operators in Python

Assignment operators are used to **assign values** to variables.

The basic assignment operator is:
    =   (single equals sign)

This operator takes the value **on the right side** and stores it in the variable **on the left side**.

Example:
    x = 10
    (Store 10 in x)

----------------------------------------------------------
🔹 Basic Example
a = 3
b = 5
c = a + b
print(c)   # Output: 8
----------------------------------------------------------

🟩 Compound Assignment Operators

Python also allows shorter forms of assignment:
Instead of writing:
    a = a + b
We can write:
    a += b

This means:
    Take the current value of a
    Add b to it
    Store the result back in a
----------------------------------------------------------

🔹 Example:
a = 3
b = 5

a += b     # same as a = a + b
print(a)   # Output: 8

----------------------------------------------------------
✨ Other Compound Assignment Operators:

a += b     → a = a + b
a -= b     → a = a - b
a *= b     → a = a * b
a /= b     → a = a / b
a //= b    → a = a // b
a %= b     → a = a % b
a **= b    → a = a ** b

These make your code shorter and cleaner.
'''

# noOfStudents =10
# noOfStudents+=1   # noOfStudents=noOfStudents+1
# # noOfStudent  11
# print(noOfStudents)

# x = 19
# y=5
# x%=y  # x=x%y
# print(x)

x =2
y=3
x**=y # x = x**y
print(x)
