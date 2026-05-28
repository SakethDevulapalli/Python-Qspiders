##Single Packing / Tuple Packing
# def temp(*args) :
#     print(args)
#     print(list(args))
#     print(type(args))

# temp(1, 2, 3, "Hi", 3,14, [10, 20], {"name" : "saketh"})

# #WAP to take multiple different types of values from the user and display only numeric values (int, float, complex) using packing.
def display(*args) :
    for i in args :
        if type(i) in [int, float, complex] :
            print(i)

display(1, 3.14, "Hi", 3+5j, [10, 20])

