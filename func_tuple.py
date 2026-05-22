## count()
## index()


## count()
## Syntax: tpl_coll.count(value)
## It is used to check how many time a value got repeated.
# tpl_coll = (1, 2, 3, 4, 1, 2, 3, 4, 5)
# print(tpl_coll.count(4)) ## 2
# print(tpl_coll.count(10))



## index()
## Syntax: tpl_coll.index(value)
## It is used to check whether the value is present inside the tuple or not. if there, it returns index value. Otherwise, it throws error.
tpl_coll = (1, 2, 3)
print(tpl_coll.index(1))
print(tpl_coll.index(10))