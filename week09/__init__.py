# name = "aya nabil"
# name1 = 'aya nabil'
# print(type(name))
# print(len(name))
# String indexing
# print(name[0])
# print(name[len(name) - 1])
# print(name[-1])
# print(name[-3]) #b

# String traversing
# for char in name :
#     print(char)

# for i in range(0,len(name)):
#     print(name[i])

# ------- String slicing
# String[start:stop:step]
# start : inclusive
# stop : execlusive
# step :
# message = "hello python , my name is aya"
# print(message[0:5:1]) #hello
# print(message[3:8:1])#lo py
# print(message[3:8:2])# l y
# print(message[0:10:3]) #hlph
# print(message[0:10]) # 1 step by defualt
# print(message[0:])  # from 0 to the end of the string
# print(message[:]) # start from 0 by defualt to the end of the string , 1 step
# print(message[-8:-1]) #e is ay
# print(message[10:0:-1])
# print(message[15 : 1 :-1])


# text = "Python programming teaches problem solving"
# print(text[0:6]) # Python
# print(text[7:18]) #programming
# print(text[-7:]) # solving
# print(text[7:]) #programming teaches problem solving
# print(text[::2]) #Pto rgamn ece rbe ovn
# print(text[::-1]) # start : length - 1 , stop : 0
# print(text[-18:-6])
# print(text[-6:-18]) # empty string
# print(text[-1:-10:-1])
# print(text[-11:])
# print(text[:-5])


# ----- String operations
# 1- String concatenation
# str1 = 'hello '
# str2='world'
# print(str1+str2)
# print(str1+2)  # TypeError

# 2- String repeatition
# print(str1*4)
# print('*'*3)

# 3 - String membership (in , not in)
# message = 'python programming language is cool'
# if 'python' in message:
#     print('python is cool')
#
# print('java' not in message)

# 4 - String comparison
#space , [0-9] , [A-Z] , [a-z]
# str1 = '1at'
# str2 = 'Cat'
# print(str1>str2)
# print("apple" <"applepie")
# print("python" >"pycharm")
# print("2nd" < "Byte")
# print("Data" > "data")

name ="python   programming    is   fun"
print(' '.join(name.split()))

