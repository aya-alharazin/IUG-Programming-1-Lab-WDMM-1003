'''
Complete Precedence Table
Priority          Operator
1 (Highest)       ()
2                 **
3                 +x, -x
4                 *, /, //, %
5                 +, -
6                 ==, !=, <, >, <=, >=
7                 not
8                 and
9                 or
10                =, +=, -=


'''
# result1 = 10 - 5 < 2 + 8 # 5   < 10
# print(result1)
# result2 = 5 + 3 > 7 and 10 - 2 < 9 # True and True
# print(result2)
# result3 = 2 * 3 == 5 or 10 / 2 == 5 #False or  True
# print(result3)
# result4 = not False and True
# print(result4)
# result5 = (10 + 5) * 2 > 15 and 20 / 4 == 5
# print(result5)
# True and True
# print("-------------------------------------------------------")
# result6 = 2 + 3 ** 2 * 4 - 10 / 2 > 20 and not 5 == 5 or 10 % 3 != 1
# # False
# print(result6)





# result7 = not 5 > 3 and 10 > 8 or 15 > 20
# print(result7)
# # False






# result8 = not (5 > 3 and 10 > 8 or 15 > 20)
# print(result8)
# not(True and True or False)
# result9 = not (5 > 3 and 10 > 8) or 15 > 20
# print(result9)
# a = b = c = 10 + 5
# result10 = 100 / 5 / 2
# print(result10)
result11 = 2 ** 3 ** 2
print(result11)
