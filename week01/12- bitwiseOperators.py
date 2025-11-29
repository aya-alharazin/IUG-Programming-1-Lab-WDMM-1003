'''
🟦 Bitwise Operators in Python (BEGINNER-FRIENDLY)

Bitwise operators work on the *binary representation* of numbers.
Python converts the numbers to binary (0s and 1s) and then applies the operation.

These operators are more advanced than logical operators,
but we can understand them with simple examples.

----------------------------------------------------------
1️⃣ Bitwise AND (&)

Rule:
1 & 1 → 1
Else → 0

Example:
a = 3   → 011 (binary)
b = 5   → 101 (binary)

011
101
---
001  → 1 (decimal)

So:
a & b  → 1

----------------------------------------------------------
2️⃣ Bitwise OR (|)

Rule:
If ANY bit is 1 → result = 1

Example:
a = 3   → 011
b = 5   → 101

011
101
---
111  → 7 (decimal)

So:
a | b  → 7

----------------------------------------------------------
🧪 Code Examples:

# Bitwise AND
a = 3   # 011
b = 5   # 101
a &= b  # same as: a = a & b
print(a)   # Output: 1

# Bitwise OR
a = 3   # 011
b = 5   # 101
a |= b  # same as: a = a | b
print(a)   # Output: 7

----------------------------------------------------------
✨ Summary for Beginners:

&  → bitwise AND  
|  → bitwise OR  

Binary of 3 = 011  
Binary of 5 = 101  

011 & 101 = 001 → 1  
011 | 101 = 111 → 7  
'''
