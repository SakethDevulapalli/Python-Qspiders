#WAP to take a number from the user and check wheather it is a prime or non-prime number. (use for loop)
'''
num = int(input("Enter a number : "))
is_prime = True
for i in range(2, num) :
    if num % i == 0 :
        is_prime = False

if is_prime:
    print("It is a prime number.")
else :
    print("It is not a prime number.")

'''

#WAP to take a number from the user and check wheather the number is strong or not. (Use while loop)

num = int(input("Enter a number : "))
add = 0
temp = num
while num != 0 :
    last_digit = num % 10
    fact = 1
    for i in range(2, last_digit + 1) :
        fact *= i
    add += fact
    num //= 10

if temp == add :
    print("Strong number")
else :
    print("Not a Strong number")