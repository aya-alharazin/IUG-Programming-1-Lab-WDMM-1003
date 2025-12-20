'''
What Are Conditional Statements?
Conditional statements allow your program to make decisions
and execute different code based on whether certain conditions are True or False.
'''
# if boolean_Exoression :
# block of code that will be executed if the condition is True
#
# 1 - Password Strength Checker (on way branch )
# password = input("Enter A password: ")
# if len(password) >= 8 :
#     print("Your password is strong")
#     print("your account is secure")
# print("Registration complete")

# 2- Login System (two way branches)
# correct_username="aya123"
# correct_password="123456"
# username = input("Enter Your username: ")
# password = input("Enter Your password: ")
#
#
# if username == correct_username and password == correct_password :
#     print("Login successful")
#     print("Welcome back")
#     print("Redireting to home page")
# else :
#     print("Login failed")
#     print("Invalid username or password")
#     print("Try again")
# print("-"*60)


# 3- grade system(Multi-way selection )
score = int(input("Enter your score: "))
if score >100 or score < 0:
    print("Invalid score")
elif  score>=90 :
    print("Grade : A")
elif  score >=80 :
    print("Grade : B")
elif  score >=70 :
    print("Grade : C")
elif  score >=60 :
    print("Grade : D")
else :
    print("Grade: F")


age =18
name ="omar"
if age >18 :
    print("your age is greater than 18")
    if name == "omar" :
        print("if_2")
    print("if_1")

















#
#
# # ATM logic needs conditionals
# balance = 1000
# withdrawal = 500
#
# if withdrawal <= balance:
#     print("✓ Transaction approved")
#     balance = balance - withdrawal
# else:
#     print("✗ Insufficient funds")
#
#
# username = "admin"
# password = "12345"
#
# if username == "admin" and password == "12345":
#     print("✓ Login successful")
# else:
#     print("✗ Invalid credentials")
#
#
# # Age checking needs conditionals
# age = 16
#
# if age >= 18:
#     print("✓ You can vote")
# else:
#     print("✗ You cannot vote yet")