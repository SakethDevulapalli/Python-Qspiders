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