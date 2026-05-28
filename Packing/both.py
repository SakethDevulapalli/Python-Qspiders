def temp(*args) :
    d= {}
    for i in args :
        d[i[0]] = i[0]
    print(d)

temp(*eval(input("Enter a dictionary : ")).items())