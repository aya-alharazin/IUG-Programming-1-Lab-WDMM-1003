'''
🟦 Type Casting in Python

Type casting means converting a value from one data type to another.

Python gives us simple built-in functions to change types:

1️⃣ int()   → Converts a value to an integer
2️⃣ float() → Converts a value to a floating-point number (decimal)
3️⃣ str()   → Converts a value into a string (text)
bool() ->Convert a value into boolean(True/False)
------------------------------------------------------------

Examples:

s = "10"
n = int(s)      # "10" → 10 (string to int)

cnt = 5
f = float(cnt)  # 5 → 5.0 (int to float)

age = 25
s2 = str(age)   # 25 → "25" (int to string)

------------------------------------------------------------
Why do we need type casting?

Because input() ALWAYS returns a string.
If we want to do math using user input, we MUST convert it to int or float.

Example:
num = float(input("Enter a number: "))
intNum = int(num)
print("The integer value of " + str(num) + " is " + str(intNum))

------------------------------------------------------------
Important Notes:
• You CANNOT add a string + number → TypeError
• Use str() to convert a number into a string before concatenation

Example:
print("Your age is " + str(age))

------------------------------------------------------------
Practice:
Take two numbers from the user and add them:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

------------------------------------------------------------
Example Problems:

Input: num = "5"
Output: 10
Explanation: Convert "5" → 5, then double it: 5 * 2 = 10

Input: num = "12"
Output: 24
Explanation: Convert "12" → 12, then double it.

'''
# int ->str
x =3
# x    3
strX=str(x)
# strX   3
print(type(strX))
print(strX)

#float -> str
price =12.4
floatPrice=str(price)
print(type(floatPrice))

# boolean ->str

# float ->int
price =12.9999999
intPrice=int(price)
print(intPrice)
#float - >str
strPrice=str(price)
print(type(strPrice))

# boolean ->str
