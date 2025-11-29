'''
🟦 Membership Operators in Python

Membership operators are used to check whether a value
EXISTS inside a sequence such as:
    • list
    • string
    • tuple
    • set

Python has TWO membership operators:

----------------------------------------------------------
1️⃣ in
   • Returns True if the value exists inside the sequence
   Example:
       "a" in "Aya"       → True
       3 in [1, 2, 3]     → True

2️⃣ not in
   • Returns True if the value does NOT exist in the sequence
   Example:
       "z" not in "Aya"   → True
       5 not in [1, 2, 3] → True

----------------------------------------------------------
🧪 Example Code:

# Membership with strings
name = "Aya"
print("A" in name)        # True
print("z" in name)        # False

# Membership with lists
numbers = [10, 20, 30]
print(20 in numbers)      # True
print(40 not in numbers)  # True

# Membership with tuples
tup = (1, 2, 3)
print(2 in tup)           # True

----------------------------------------------------------
✨ Summary for Beginners:

in       → checks if an item EXISTS inside a sequence
not in   → checks if an item DOES NOT exist inside a sequence

Used with:
• strings
• lists
• tuples
• sets
• dictionaries (checks keys)

----------------------------------------------------------
'''
