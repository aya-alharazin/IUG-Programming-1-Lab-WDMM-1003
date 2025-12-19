'''
🐍 1. input() Function in Python :
The input() function is used when you want your program to ask
the user for information while the program is running.
⭐ 2. What Is a Prompt?
The text inside the input function is called a prompt.
⭐ 3. Input Always Comes as a String
Even numbers are returned as text.
Ex :
1- ask the user for his name
input : what is your name ? Nour
output:Hey Nour , How are u?
'''
# Hi Ahmed
# your current age is 40 , after 10 years you'll be 50
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hi "+name)
ageAfter10years=int(age)+10
print("your current age is "+age+", after 10 years you'll be "+str(ageAfter10years))

# int + str -> ivalid
#str +str   -> valid concatenation
#int + int  -> addition