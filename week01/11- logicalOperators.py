'''
🟦 Logical Operators in Python (Beginner-Friendly)

Logical operators are used to combine conditions.
They ALWAYS return:
    ✔ True 
    ✘ False

They are most commonly used inside if-statements.

----------------------------------------------------------
Logical Operators:

1️⃣ and  
   • Returns True ONLY if BOTH conditions are True
   Example:
       (5 > 2 and 10 > 3) → True
       (5 > 2 and 1 > 3)  → False

2️⃣ or  
   • Returns True if AT LEAST ONE condition is True
   Example:
       (5 > 10 or 10 > 3) → True
       (2 > 5 or 1 > 3)   → False

3️⃣ not  
   • Reverses the condition
       True  → False
       False → True
   Example:
       not True  → False
       not False → True

----------------------------------------------------------
🧪 Example Code:

x = 10
y = 5

print(x > 5 and y < 10)   # True
print(x == 5 or y == 5)   # True
print(not (x > y))        # False

----------------------------------------------------------
✨ Summary:
• and → both conditions must be True  
• or  → at least one condition must be True  
• not → reverses True/False  
'''