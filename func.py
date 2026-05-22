## 1. Take 2 lists
## 2. Find out the common values,
## 3. Store them inside a list
## 4. return it
# def comm_values(coll1, coll2):
#     comm_val = []
#     for i in coll1:
#         if i in coll2:
#             comm_val.append(i)
#     return comm_val

# result = comm_values([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
# print(result)

# print(comm_values([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))






# def addTwoNums(a, b):
#     print(a, b)
#     print(a, b)
#     return a + b

# print(addTwoNums(10, 5)) ## (10, 5)





## None

# def greeting():
#     print('Hey! There')

# # var = greeting()
# # print(var)

# print(greeting())


## var_name.lower() / string.lower()
# s = 'PYTHON@123'
# l = s.lower()
# print(l)
# print(id(s) == id(l))

## var_name.upper()
# s = 'python@123'
# print(s.upper())

## islower()
## isupper()
## isalpha()
## isdigit()
## isalnum()


## lower()
## Syntax: var_name.lower() or, string.lower()
## It converts alphabets into lower case alphabets.


## upper()
## Syntax: var_name.upper() or, string.upper()
## It converts alphabets into upper case alphabets.


## islower()
## Syntax: var_name.islower() or, string.islower()
## It returns True if the string consists of lower case alphabets. Otherwise, False.
# print('python'.islower()) ## True
# print('Python'.islower()) ## False
# print('Python@123'.islower()) ## False


## isupper()
## Syntax: var_name.isupper() or, string.isupper()
## It returns True if the string consists of upper case alphabets. Otherwise, False.
# print('python'.isupper()) ## False
# print('PYTHON'.isupper()) ## True
# print('PYTHON@123'.isupper()) ## True


## isalpha()
## Syntax: var_name.isalpha() or, string.isalpha()
## It returns output as True if and only if the string consists of alphabets. Otherwise, False.
# print('python'.isalpha()) ## True
# print('python@123'.isalpha()) ## False
# print('Python'.isalpha()) ## True
# print('1234@'.isalpha()) ## False


## isdigit()
## Syntax: var_name.isdigit()
## It returns True if the string consists of only digits. Otherwise, False.
# print('09876'.isdigit()) ## True
# print('python@123'.isdigit()) ## False


## isalnum()
## Syntax: var_name.isalnum() or, string.isalnum()
## It checkes whether the string consists of only alphabets or digits or not.
# print('python123'.isalnum())
# print('python'.isalnum())
# print('0987'.isalnum())
# print('0987@'.isalnum())


## startswith()
## Syntax: var_name.startswith(subStr) or, string.startswith(subStr)
## It returns True if the string starts with the given substr. Otherwise False.
# print('Programming'.startswith('Pro'))


## endswith()
## Syntax: var_name.endswith(subStr) or, string.endswith(subStr)
## It returns True if the string ends with the given substr. Otherwise False.
# print('Programming'.endswith('G'))


## index()
## Syntax: var_name.index(substr) or, string.index(substr)
## It checkes whether the substr is present inside the original string or not. If present, returns index no. Otherwise, error.
# print('python'.index('p')) ## 0
# print('python'.index('on')) ## 4
# print('python'.index('Z')) ## ERROR
# print('Hello, World!'.index('o', 5))



## find()
## Syntax: var_name.find(substr) or, string.find(substr)
## It checkes whether the substr is present inside the original string or not. If present, returns index no. Otherwise, returns -1.
# print('python'.find('p')) ## 0
# print('python'.find('on')) ## 4
# print('python'.find('Z')) ## ERROR
# print('Hello, World!'.find('o', 5)) ## 8
# print('python'.find('X')) ## -1


## strip()
## Syntax: var_name.strip() or, string.strip()
## It is used to remove white spaces from the beginning and ending of a string.
s = '  python  '
# print(len(s))
# print(s.strip(), len(s.strip()))


## lstrip()
## Syntax: var_name.lstrip() or, string.lstrip()
## It removes white spaces from the beginning of the string.
# print(s, len(s))
# print(s.lstrip(), len(s.lstrip()))


## rstrip()
## Syntax: var_name.lstrip() or, string.lstrip()
## It removes white spaces from the ending of the string.
# print(s, len(s))
# print(s.rstrip(), len(s.rstrip()))


## capitalize()
## Syntax: var_name.capitalize() or, string.capitalize()
## It converts the first character of a string into upper case and remaining into lowercase.
# print('I LOVE PYTHON PROGRAMMING LANGUAGE'.capitalize())
# print('python'.capitalize())


## title()
## Syntax: var_name.title() or, string.title()
## It converts the starting character of each and every word into uppercase and remaining into lowercase of a string.
# print('I LOVE PYTHON PROGRAMMING LANGUAGE'.title())
# print('python'.title())


## swapcase()
## Syntax: var_name.swapcase() or, string.swapcase()
## It converts uppercase alphabets into lowercase and lowercase alphabets into uppercase. It keeps the special characters and digits as it is of a string.
# print('Python@123'.swapcase())
# print('@123'.swapcase())
# print('PyThOn'.swapcase())


## replace()
## Syntax: var_name.replace(old, new) or, string.replace(old, new)
## It is used to replace the old substr with a new substr.
# print('python'.replace('p', 'P'))
# print('python'.replace('python', 'PYTHON'))
# print('PYTHON'.replace('PYTHON', 'python'))


## split()
## Syntax: var_name.split(subStr) or, string.split(subStr)
## It is used to splitted out a string by using the given subStr.
# s = 'I Love Python Programming Language'
# print(s.split('Python'))


## join()
## Syntax: subStr.join(coll)
## It is used to concatinate all the individual strings into a single string by using subStr.
s = ['I', 'Love', 'Python', 'programming', 'Language']
print(' '.join(s))
print('-@-'.join(s))