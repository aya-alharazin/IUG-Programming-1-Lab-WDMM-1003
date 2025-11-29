'''
🟦 Identity Operators in Python

Identity operators are used to check
whether **two variables refer to the same object in memory**, not just equal value.

Python has two identity operators:

----------------------------------------------------------
1️⃣ is
   • Returns True if both variables refer to the SAME object
   • Not just same value — SAME memory location

2️⃣ is not
   • Returns True if both variables refer to DIFFERENT objects

----------------------------------------------------------
🧠 Important:
Identity operators check **memory identity**, not value equality.

For equality check (same value), use:
    ==   and   !=

For identity check (same object), use:
    is   and   is not
----------------------------------------------------------

🧪 Examples:

# Example 1: Same value, SAME memory object (small integers are cached)
a = 5
b = 5
print(a is b)        # True
print(a == b)        # True

# Example 2: Same value, DIFFERENT objects (lists are not shared)
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)        # True   → same value
print(x is y)        # False  → different objects

# Example 3: is not
name1 = "Aya"
name2 = "Doaa"
print(name1 is not name2)   # True

----------------------------------------------------------
✨ Summary for Beginners:

==       → check if values are equal
!=       → check if values are NOT equal

is       → check if both variables refer to the SAME object in memory
is not   → check if they refer to DIFFERENT objects

----------------------------------------------------------
'''