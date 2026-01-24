'''
Program 1: Reverse a string using slicing
'''
# message = "keep going dont stop"
# reversed_message = message[::-1]
# print(reversed_message)
'''
Program 2: Remove digits from a string
'''
# name = 'a1ya 1nabil 2025salee3m'
# result = ""
# for char in name:
#     if '0' <= char <= '9' : # space [0-9] [A-Z] [a-z]
#         continue
#     result += char
# print(result)

'''
Program 3: print every second letter in reverse
input : aya nabil
output : lbnaa
'''
name = "aya nabil"
result = name[::-2]
print(result)

'''
---------- String Methods -------------
1. CAPITALIZE - Make the first letter uppercase
   -----------------------------------------------
   Write a program that takes a sentence and makes only the first letter uppercase.
   The rest of the letters should stay as they are.

   Input: "hello world My NaMe Is AyA AnD I LoVe PyThOn"
   Output: "Hello world my name is aya and i love python"
'''

# message = "hello world My NaMe Is AyA AnD I LoVe PyThOn"
# message1 = message.capitalize()
# print(message1)
# print(message)

'''
2. COUNT - Count how many times a letter appears
   -----------------------------------------------
   Count how many times the letter 'a' appears in the word "banana".

   Input: "banana"
   Output: 3
'''
# message = "banana"
# count_letter_a = message.count('a')
# print(count_letter_a)
#
# message = "python is cool , I love python , python is great"
# print(message.count("python"))

'''
3 - startswith , endswith
Write a Python function that take a url and checks the following:

If the URL starts with https:// and ends with .edu, print:
Secure educational website

If the URL starts with https:// only, print:
Secure website only

If the URL ends with .edu only, print:
Educational website only

Otherwise, print:
Unsecure or non-educational website
'''
def url_validate(url):
    if url.startswith('https://') and url.endswith('.edu') :
        print('Secure educational website')
    elif url.startswith('https://'):
        print('Secure website only')
    elif url.endswith('.edu'):
        print('Educational website only')
    else:
        print('Unsecure and non-educational website')

url_validate('http://aya.ed')



'''
4 - find , rfind 
Extract file extension using find
'''
# file = input("enter file name") # aya.pdf
# dot_index = file.rfind('.')
# file_extension = file[dot_index+1:]
# print(file_extension)


'''
5 - index , rindex 
using index function
'''
# file = input("enter file name") # aya.pdf
# dot_index = file.index('.')
# file_extension = file[dot_index+1:]
# print(file_extension)

'''
Note - the difference between find and index
'''
# str = 'aya nabil'
# print(str.find('s')) # return -1 if the substring does not exsits
# print(str.index('s')) # return ValueError
'''
5 - isalpha() , isdigit()
Count letters and digits in a string 
'''
str = 'aya 2025nabil2001'
letter_count = 0
digit_count=0
for char in str :
    if char.isalpha():
        letter_count+=1
    elif char.isdigit():
        digit_count+=1

print("digit count", digit_count)
print("letter count" , letter_count)

# print('12345'.isdigit())
# print('1234b3'.isdigit())
# print('a1ya'.isalpha())
'''
6 - islower() , isupper() , lower() , upper()
swap Case
    -------------
    Loop through a string and swap the case of each letter.
    (Uppercase becomes lowercase, lowercase becomes uppercase)

    Input: "Hello World"
    Output: "hELLO wORLD"
'''
str = "Hello World"
result = ""
for char in str :
    if char.islower():
        result+=char.upper()
    elif char.isupper():
        result+=char.lower()
    else :
        result+=char
print('result' , result)
'''
7 -  STRIP - Remove extra white spaces from string
'''

# name = '     aya     \t\n  '
# print('['+name.strip()+']')
# print('['+name.lstrip()+']')
# print('['+name.rstrip()+']')






'''


8 - REPLACE - Replace spaces with underscores
    -------------------------------------------
    Replace all spaces in the sentence with underscores (_).
    Input: "Hello from string lecture"
    Output: "Hello_from_string_lecture"
'''
# str = "Hello from string lecture , string is very cool"
# print(str.replace(" " , "_"))
# print(str.replace("string" , "python"))

'''
9 - Split Function
'''
name = "Aya_Nabil_Saleem_Alharazin" #A.N.S.A.
initials= ""
list = name.split('_')
for word in list:
    initials = initials + word[0] + '.'

'''
10 - join 
'''
name = "Aya_Nabil_Saleem_Alharazin"
list = name.split("_")
joinedList = ' '.join(list)
print(joinedList)