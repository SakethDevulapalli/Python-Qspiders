# def addTwoNums(n1, n2) :
#     print("n1 : ", n1)
#     print("n2 : ", n2)
#     print(n1 + n2)
    
# coll = (100, 200)
# addTwoNums(*coll)


def addNums(*args) :
    add = 0
    for i in args :
        add += i
    print(add)
addNums(*eval(input("Enter a list of numbers : ")))