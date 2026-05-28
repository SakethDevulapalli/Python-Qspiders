# ##WAP using recursion to reverse a number.
# #Regular process
# num = int(input("Enter a number : "))
# result = 0
# while num != 0 :
#     result = result*10 + num%10
#     num //= 10
# print(result)

##OR

# ##using Resursion
# def reverse(num, result = 0) :
#     if num == 0 :
#         return result
#     result = result*10 + num%10
#     num //= 10
#     return reverse(num, result)
# print(reverse(int(input("Enter a number : "))))



##WAP to find largest digit of a number
# list = eval(input("Enter a number : "))
# lar_num = list[0]
# i = 0
# while i < len(list) :
#     if list[i] > lar_num     :
#         lar_num = list[i]
        
#     i += 1
# print(lar_num)

##OR

# def lar_number(list, lar_num=float('-inf'), i=0) :
#     if i >= len(list) :
#         return lar_num
#     if list[i] > lar_num     :
#         lar_num = list[i]
#     i += 1
#     return lar_number(list, lar_num, i)
# print(lar_number(eval(input("Enter a number : "))))


##WAP using recursion to check whether the number is a perfect number or not.
# num = int(input("Enter a number : "))
# result = 0
# i = 1
# while i < num :
#     if num % i == 0 :
#         result += i
#     i += 1
# if result == num :
#     print("Yes!")
# else :
#     print("No!")

##OR

# def perfect(num, result=0, i=1) :
#     if i >= num :
#         return result
#     if num % i == 0 :
#         result += i
#     i += 1
#     return perfect(num, result, i)

# def is_perfect(num) :
#     return "Perfect number" if num == perfect(num) else "Not a perfect number"
# print(is_perfect(int(input("Enter a number : "))))


