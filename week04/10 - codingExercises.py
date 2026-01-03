# 1 - even or odd

# num = int(input("Enter a number: "))
# # num % 2 == 0  ---> even
# if num % 2 == 0 :
#     print(num,"is even")
# else :
#     print(num,"is odd")
#
# print('enter a valid number')
# ---------------------------------------------------------------------
# 2- Enter a year and check if it is a leap or not
# year = int(input("Enter a year: "))
# if year % 4 == 0 :
#     if year % 100 ==0 :
#         if year % 400 ==0 :
#             print(year,"is a leap year")
#         else :
#             print(year,"is not a leap year")
#     else :
#         print(year,"is a leap year")
# else :
#     print(year,"is not leap")
# --------------------------------------------------
# 3- 🍕 Pizza Order System
pizzaSize = int(input("What size of pizza do you want:\n1-Small\n2-Meduim\n3-Large\nEnter your choice (1/2/3): "))
totalPrice = 0
if pizzaSize == 1 :  # small size
    totalPrice +=100
    needApaparoni = input("do you need a paparoni : (y ,n) ")
    if needApaparoni == "y" :
        totalPrice+=30
else :
    if pizzaSize == 2:
        totalPrice += 200
    elif pizzaSize == 3:
        totalPrice += 300
    else:
        print("the number does not valid !!")
    needApaparoni = input("do you need a paparoni : (y ,n) ")
    if needApaparoni == "y":
        totalPrice += 50
extraCheese = input("do you need an extra cheese (y ,n): ")
if(extraCheese == "y"):
    totalPrice += 20

print(f"final price is {totalPrice}")

# 4- the largest number from 3 numbers
# num1 = int(input("Enter The first number : "))
# num2 = int(input("Enter The second number : "))
# num3 = int(input("Enter The third number : "))

# num1 >= num2    and num1 >= num3       ----->  num1 is the largest
# num2 >= num3                          ------>   num2 is the largest
#                                      ------->  num3 is the largest

# if num1 >= num2 and num1 >= num3:
#     print(num1 ,"is the largest number")
# elif num2 >=num3 :
#     print(num2 , "is the largest number")
# else :
#     print(num3 , "is the largest number")

