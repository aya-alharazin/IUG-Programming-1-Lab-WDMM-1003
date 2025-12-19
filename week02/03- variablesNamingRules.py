'''
📌 Rules for Naming Variables in Python (Beginner-Friendly)

1️⃣ Variable names can only contain:
    - Letters (a–z, A–Z)
    - Digits (0–9)
    - Underscores (_)

    ✔ Valid: name, age1, user_name
    ✘ Invalid: user-name, user name, @age

------------------------------------------------------------

2️⃣ A variable name CANNOT start with a number.

    ✔ Valid: name1, age_22
    ✘ Invalid: 1name, 22_age

------------------------------------------------------------

3️⃣ Variable names are CASE-SENSITIVE.
    This means:
        myVar, MyVar, MYVAR → all different variables

------------------------------------------------------------

4️⃣ Do NOT use Python keywords as variable names.
    Keywords are special reserved words like:
        if, else, for, while, class, True, False, None

    ✘ Invalid: if = 3
    ✔ Valid: number_if = 3

------------------------------------------------------------

5️⃣ Variable names should be MEANINGFUL.
    ✔ name, age, studentID
    ✘ a, x1, test123  (not clear for others)

------------------------------------------------------------

6️⃣ For multi-word variable names, use one of these styles:

    ✔ Snake Case     → student_name    (recommended in Python)
    ✔ camelCase      → studentName
    ✔ PascalCase     → StudentName

------------------------------------------------------------

✨ Summary:
Choose clear, readable, meaningful names that follow Python rules.
'''


name = "aya"
# name "aya"
Name = "Ahmed"
# Name "Ahmed"
print(name)
print(Name)

x = 1.7

is_graduate =True #snake_case
isAyaGraduate = False # camelCase
IsAyaGraduate = True  #PascalCase
