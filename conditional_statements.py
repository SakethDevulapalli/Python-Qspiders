'''  <--- IF STATEMENT --->  '''

# WAP to take the age from the user and check wheather the user is adult or not. If adult, display "You are eligible for driving".
'''
1. Take input from the user in the from of age.
2. If we use input only it provides the output in string format, so type cast the input function.
3. check wheather the user is adult or not.
4. If the user is adult, display "You are eligible for driving". 
'''

'''
age = int(input("Enter your age : "))
if age >= 18 :   #condition
    print("you are eligible for driving.")  #true statement block
'''



#WAP to take an int number from the user and check wheather it is even or odd. If even, display True.
'''
num = int(input("Enter a number : "))
if (num%2) == 0 :   #condition
    print(True)   #true statement block
'''


# WAP to take random value from the user and check wheather the value is single value datatype or multi value datatype.If SVDT, display True.
'''
num = eval(input("Enter a random number : "))
svdt = [int, float, complex, bool]
if type(num) in svdt :
    print(True)
'''



'''  <--- IF-ELSE STATEMENT --->  '''


#WAP to take any random character from the user and check wheather it is vowel or not. If vowel, display True. otherwise, False.
'''
1. Take any random character from the user.
2. Check wheather the character is vowel or not.
3. If vowel, print(true)
4. If not, print(false)
'''

'''
vowel = ['a', 'e', 'i', 'o', 'u']
char = input('Enter your character : ')
if char in vowel:
    print("True")
else :
    print("False")
'''

#WAP to take a string from the user and check wheather it is even length string or not. If even length string then display its reverse. Otherwise, display the string as it is.
'''
1. Take a string as an input from the user.
2. we have to check wheather it is even length string or not.
3. If even, print its reverse.
4. Otherwise, print the string as it is.
'''

'''
word = input("Enter your random word : ")

if (len(word) % 2) == 0 :
    print(word[: : -1])
else :
    print(word)
'''


#WAP to take a number from the user and check wheather it is positive or negative. If positive, print("Positive"). Otherwise, print("Negative")
'''
num = int(input("Enter a random number : "))
if num >= 0 :
    print("Positive")
else :
    print("Negative")
'''


#WAP to take a character from the user and check wheather it is an alphabet or, a digit or, a special character.
'''
char = input("Enter a character : ")
if 'A' <= char <= 'Z' or 'a' <= char <= 'z' :
    print("alphabet")
elif char in '0123456789' :
    print("Digit")
else :
    print("Special Character")
'''


'''     <--- Nested-IF STATEMENT --->     '''


'''
WAP to take any random character from the user and check:
1.Wheather it is alphabet, then check wheather it is vowel or consonent.
    - If vowel then print "Vowel"
    - otherwise, print "consonent"
2. If not an alphabet then:
    - If digit, print "Digit"
    - otherwise, print "Special character"
'''

'''
char = input("Enter a character : ")
if 'A' <= char <= 'Z' or 'a' <= char <= 'z' :
    if char in 'aeiouAEIOU' :
        print("Vowel")
    else :
        print("Consonent")
else :
    if char in '0123456789' :
        print("Digit")
    else :
        print("Special Character")
'''



#WAP to take any character from the user and check:
'''
1. Wheather it is alphabet or not.
    a. If alphabet then check wheather it is an "uppercase" or "lowercase" alphabet.
        - If "uppercase" then convert it into "lowercase" and print it.
        - If "lowercase" then convert it into "uppercase" and print it.
2. If not an alphabet then print "provide one alphabet".
'''
'''
alph = input("Enter a alphabet : ")
check = ord(alph)
if 'A' <= alph <= 'Z' or 'a' <= alph <= 'z' :
    if 65 <= check <= 90 :
        print(chr(ord(alph)+32))
    elif 97 <= check <= 122 :
        print(chr(ord(alph)-32))
else :
    print("Provide Alphabet")
'''



#WAP to take random int numbers and check wheather the 2nd last digit of the number is an even digit or odd digit.
'''
-   If even digit, then print the square of the 2nd last digit.
-   If odd digit, then print the cube of the 2nd last digit.
'''
'''
digit = int(input("Enter a random digit : "))
str_num = str(digit)
if len(str_num) >= 3 :
    second_last_digit = (digit//10)%10
    if second_last_digit%2 == 0 :
        print(second_last_digit * second_last_digit)
    elif second_last_digit%2 != 0 :
        print(second_last_digit * second_last_digit * second_last_digit)
else :
    print("Not a 3 digit number.")
'''

'''    <---  WHILE LOOP  --->   '''

#WAP to print numbers from 1 to 10 using a while loop.
'''
i = 1
while i<= 10 :
    print(i, end = " ")
    i += 1
'''
#WAP  to print numbers from 10 to 1 in reverse order
'''
i = 10
while i >= 1 :
    print(i, end=" ")
    i -= 1
'''

#WAP to print all even numbers from 1 to 50
'''
i = 1
while i <= 50 :
    if i%2 == 0 :
        print(i, end=" ")
    i += 1
'''

#WAP to print all odd numbers from 1 to 50
'''
i = 1
while i <= 50 :
    if i%2 != 0 :
        print(i, end=" ")
    i += 1
'''

#WAP to find the sum of the first 10 natural numbers using a while loop
'''
i = 1
sum = 0
while i <= 10 :
    sum += i
    i += 1
print(sum)
'''

# Write a program to calculate the factorial of a number using a while loop.
'''
i = 5
fact = 1
while i >= 1 :
    fact *= i
    i -= 1
print(fact)
'''

# Write a program to count the number of digits in a given number.

num = 2345



# Write a program to reverse a number using a while loop.
'''
num = 2345
str_num = str(num)
print(str_num[ : : -1])
'''



# Write a program to print the multiplication table of a given number using a while loop.
'''
num = 5
i = 1
while i <= 10 :
    print(num*i)
    i += 1
'''    
