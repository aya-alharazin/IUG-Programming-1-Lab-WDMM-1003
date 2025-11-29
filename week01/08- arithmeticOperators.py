'''
🟦 Arithmetic Operators in Python

1️⃣ Addition (+)
   x + y → adds two numbers

2️⃣ Subtraction (-)
   x - y → subtracts y from x

3️⃣ Multiplication (*)
   x * y → multiplies two numbers

4️⃣ Division (/)
   x / y → normal (float) division
           ALWAYS returns a decimal (float), even if the result is whole.
           Example: 10 / 5 = 2.0

5️⃣ Floor Division (//)
   x // y → integer division (cuts off the decimal part)
            Example: 10 // 3 = 3

6️⃣ Modulus (%)
   x % y → gives the remainder of the division
           Example: 10 % 3 = 1

7️⃣ Exponent (**)
   x ** y → raises x to the power of y
            Example: 2 ** 3 = 8

----------------------------------------------------------
🟩 Division Operators (Very Important)

In Python, we have TWO division operators:

1. Float Division ( / )
   - Always returns a float
   - Example: 7 / 2 = 3.5

2. Floor Division ( // )
   - Returns an integer (drops the decimal)
   - Example: 7 // 2 = 3

----------------------------------------------------------
✨ Summary:
• /  → float division
• // → integer floor division
• %  → remainder
• ** → power
'''

x = 10
y = 5

add = x + y        # 15   → Addition
sub = x - y        # 5    → Subtraction
mul = x * y        # 50   → Multiplication
div = x / y        # 2.0  → Float division
floorDiv = x // y  # 2    → Floor (integer) division
mod = x % y        # 0    → Modulus (remainder)
exp = x ** y       # 100000 → Exponent (10^5)

print(add)
print(sub)
print(mul)
print(div)
print(floorDiv)
print(mod)
print(exp)

