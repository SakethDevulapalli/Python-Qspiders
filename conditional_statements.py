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
char = input("Enter a character : ")
if 'A' <= char <= 'Z' or 'a' <= char <= 'z' :
    print("alphabet")
elif char in '0123456789' :
    print("Digit")
else :
    print("Special Character")