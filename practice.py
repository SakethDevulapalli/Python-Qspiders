#PRACTICE

'''
#WAP TO TAKE THE AGE FROM THE USER AND CHECK WHETHER THE USER IS ADULT OR NOT. IF ADULT, DISPLAY "YOU ARE ELIGIBLE FOR DRIVING".
age = int(input("Enter your age : "))
if age > 18 :
    print("You are eligible for driving.")

else :
    print("you are not eligible for driving.")

'''

'''
#WAP to take an int number from the user and check whether it is even or odd. if even, display true.
num = int(input("Enter a number : "))
if num % 2 == 0 :
    print("True")
else :
    print("False")
'''

'''
#WAP to take random value from the user and check whether the value is either SVDT or MVDT. if svdt, display true.
num = eval(input("Enter a value :"))
svdt = [int, float, complex, bool]
if type(num) in svdt :
    print("SVDT")
else :
    print("MVDT")
'''

'''
#WAP to take any random charater from the user and check whether it ir vowel or not. If vowel, display true. Otherwise, False.
char = input("Enter a character : ")
vowel = ['a', 'e', 'i', 'o', 'u']
result = False
if char in vowel :
    result = True
else :
    result = False
print(result)
'''

'''
#WAP to take a string from the user and check whether it is even length string or not. If even length string then display its reverse.
String = input("Enter a string : ")
check = len(String)
if check % 2 == 0 :
    print(String[ : : -1])'''

'''
#WAP to take a number from the user and check whether it is positive or negative or zero. If positive, print positive. Otherwise print("Negative").
num = int(input("Enter a number : "))
if num >= 0 :
    print("Positive")
else : 
    print("Negative")
'''    

'''
#WAP to take a character from the user and check whether it is an alphabet or a digit, or a special character.
char = input("Enter a character : ")
if 'A' <= char <= 'Z' or 'a' <= char <= 'z' :
    print("Alphabet")
elif char in '0123456789' :
    print("Digit")
else :
    print("Special Character")
'''

'''
#WAP to take any random character from the user and check:
    1. Whether it alphabet or not
        a. if alphabet, then check whether it is vowel or consonant.
        - if vowel then print "vowel"
        - else print "consonent"
    2. If not an alphabet then 
        a. check whether it is digit or special character.
        - if digit print digit.
        - else print special character.    
''''''
char = input("Enter a character : ")
check = ['a', 'e', 'i', 'o', 'u']
if 'A' <= char <= 'Z' or 'a' <= char <= 'z' :
    if char in check :
        print("VOWEL")
    else :
        print("CONSONANT")
elif char in '0123456789' :
    print("DIGIT")
else :
    print("SPECIAL CHARACTER")'''



#WAP to take any charcter from the user and check:
#   1. whether it is alphabet or not
#       a. If alphabet then check whether it is an "uppercase or"    

'''
#WAP to find the factioral of a number
num = int(input("Enter a number : "))
fact = 1

for i in range(num) :
    fact *= num
    num -= 1

print(fact)
'''

'''
#WAP to check whether the number is palindrome or not
num = int(input("Enter a number : "))
temp = num
rev = 0
while num != 0 :
    last_digit = num % 10
    rev = rev * 10 + last_digit
    num = num//10

if temp == rev :
    print("Palindrome")
else :
    print("Not a palindrome")
'''

'''
#WAP to check whether it is a strong number or not.
num = int(input("Enter a number : "))
temp = num
fact = 1
result = 0

while num != 0 :
    last_digit = num % 10
    for i in range(last_digit) :
        fact *= last_digit
        last_digit -= 1
    result = result+fact
    num = num // 10
    fact = 1

if result == temp :
    print("Strong number")
else :
    print("Not a strong number")
'''


#WAP to check whether it is a arnstrong number or not.
num = int(input("Enter a number : "))
temp = num
count = 0
val = 0
while num != 0 :
    num = num // 10
    count += 1

while num != 0 :
    last_digit = num % 10
    val = val + last_digit**count
    temp = num // 10

if val == temp :
    print("Armstrong")






#WAP to check whether it is a perfect number or not.
#WAP to check whether it is a harshad number or not.