## append()
## insert()
## extend()
## pop()
## remove()
## copy()
## index()
## count()
## clear()
## sort()
## reverse()



## append()
## Syntax: list_coll.append(val)
## It is used to add a new value at the end of an existing list collection. At a time we can add exactly a single value.
# list_coll = [1, 2, 3, 4, 5]
# print('Before:', list_coll)
# list_coll.append(6) ## Single
# list_coll.append(10, 20)
# print('After:', list_coll)
'''
Before: [1, 2, 3, 4, 5]
After: [1, 2, 3, 4, 5, 6]
'''


## insert()
## Syntax: list_coll.insert(index, value)
## It is used to add a new value at a specific index. At a time we can add exactly one value.
# list_coll = [1, 2, 3, 4, 5] ## 0, 1, 2, 3, 4
# print('Before:', list_coll) ## [1, 2, 3, 4, 5]
# list_coll.insert(1, 20) ## [1, 20, 2, 3, 4, 5]
# list_coll.insert(2, 30) ## [1, 20, 30, 2, 3, 4, 5]
# print('After:', list_coll) ## [ 1, 20, 30, 2, 3, 4, 5 ]
'''
Before: [1, 2, 3, 4, 5]
After: [1, 20, 30, 2, 3, 4, 5]
'''



## extend()
## Syntax: list_coll.extend(coll_of_values)
## It is used to add multiple values inside an existing list collection.
# list_coll = [1, 2, 3]
# print('Before:', list_coll)
# list_coll.extend([4, 5, 6])
# print('After:', list_coll)



## pop()
## Syntax: list_coll.pop(index=-1)
## It is used to eliminate value from a particular index. If no index given then it will always eliminate value from the end.
# list_coll = [1, 2, 3, 4, 5]
# print('Before:', list_coll)
# list_coll.pop(2)
# list_coll.pop()
# print('After:', list_coll)



## remove()
## Syntax: list_coll.remove(value)
## It is used to remove the first occurence of a given value. 
# list_coll = [1, 2, 3, 4, 5, 1, 2]
# list_coll.remove(2)
# list_coll.remove(1)
# list_coll.remove(10)
# print(list_coll)


## copy()
## Suntax: dest_var = source_var.copy()
## It is used to perform shallow copy operation.
# list1 = [1, 2, 3, 4]
# list2 = list1.copy()
# print(id(list1))
# print(id(list2))


## index()
## Syntax: list_coll.index(value)
## It is used to check whether the value is present inside the list collection or not. If present, then it returns the index number. Otherwise, it throws error.
# list_coll = [1, 2, 3, 4, 5]
# print(list_coll.index(4))
# print(list_coll.index(10)) ## Error



## count()
## Syntax: list_coll.count(value)
## It is used to check how many time a particular value got repeated.
# list_coll = [1, 2, 3, 4, 5, 2, 3]
# print(list_coll.count(1)) ## 1
# print(list_coll.count(3)) ## 2
# print(list_coll.count(30)) ## 0



## clear()
## Syntax: list_coll.clear()
## It is used to remove all the values from a list collection and make the list empty.
# list_coll=[1, 2, 3]
# list_coll.clear()
# print(list_coll) ## []



## sort()
## Syntax: list_coll.sort(reverse=False)
## It is used to arrange all the list values either in ascending or descending order.
## By default, list values will be sorted in ascending order. If we want to sort them in descending order then we have to change the value of "reverse" into True (reverse=True).
# list_coll = [3, 1, 2, 5, 4]
## Ascending
# list_coll.sort()
## Descending
# list_coll.sort(reverse=True)
# print(list_coll)




## reverse()
## Syntax: list_coll.reverse()
## It is used to reverse the value of a list collection.
# list_coll = [3, 1, 2, 5, 4]
# print('Before:', list_coll)
# list_coll.reverse()
# print('After:', list_coll)
# help(list.reverse)
