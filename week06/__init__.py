# Question 1
# def sum_of_digits(num): #1234
#     sum_digit = 0
#     while num > 0:
#         last_digit = num%10  # 1
#         sum_digit = sum_digit +last_digit # sum_digit =0+4+3+2+1
#         num = num //10 #0
#     return sum_digit
#
# num = int(input("Enter a number: "))
# result = sum_of_digits(num)
# print(f"the number is {num} and the sum is {result}")
#---------------------------------------------------------------
#Question 3
# def reverse_number(num):#1234
#     rev =0
#     while num >0 :
#         last_digit=num%10
#         rev = (rev*10)+last_digit # rev =4321
#         num=num//10
#     return rev
#
# num = int(input("Enter a number: "))
# result = reverse_number(num)
# print(f"the number is {num} and the reverse is {result}")
#--------------------------------------------------------------
# Question 5
# def is_prime(num):
#      counter = 0
#      for i in range(1,num+1):
#          if num % i ==0 :
#              counter+=1
#      if counter ==2 :
#          return True
#      else:
#          return False
#
# num = int(input("Enter a number: "))
# result = is_prime(num)
# print(result)

# ----------------------------------------------------------
# Question 7
# for i in range(1,6):
#     print('*'*i)

#----------------------------------------------------------
# Question 8
# sum_digit =0
# while True :
#     num = int(input("Enter a number: "))
#     if num<0:
#         break
#     else:
#         sum_digit = sum_digit + num
#
# print(f"the sum is {sum_digit}")

#--------------------------------

for i in range(1,21):
    if i%3==0:
        continue
    print(i)










