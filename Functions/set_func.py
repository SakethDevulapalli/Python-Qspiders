## add()
## clear()
## copy()
## difference()
## discard()
## intersection()
## issubset()
## issuperset()
## pop()
## remove()
## symmetric_diference()
## union()
## update()




## add()
## Syntax: coll.add(val)
## It is used to add a new value inside an existing set collection.
# coll = {1, 2, 3, 4, 5}
# coll.add(6)
# coll.add(7, 8) ## Error.
# print(coll)



## clear()
## Syntax: coll.clear()
## It is used to remove all the values from a set collection and make it empty set.
# coll = {1, 2, 3, 4, 5}
# coll.clear()
# print(coll) ## set()




## copy()
## Syntax: var = coll.copy()
## It is used to perform shallow copy.
# coll1 = {1, 2, 3, 4, 5}
# coll2 = coll1.copy()
# print('Coll1:', id(coll1))
# print('Coll2:', id(coll2))




## pop()
## Syntax: coll.pop()
## It is used to remove value from an existing set collection randomly.
# coll = {1, 2, 3, 4, 5}
# coll.pop()
# coll.pop()
# print(coll)
# help(set.pop)



## remove()
## Syntax: coll.remove(value)
## It is used to remove a particular value from an existing set collection.
# coll = {1, 2, 3, 4, 5}
# coll.remove(3)
# coll.remove(4)
# coll.remove(10)
# print(coll)



## discard()
## Syntax: coll.discard(value)
## It is used to remove a particular value from an existing set collection. if the value is not present, it will not throw any error.
# coll = {1, 2, 3}
# coll.discard(5)
# coll.discard(3)
# print(coll)




## update()
## Syntax: coll.update(iterable)
## It is used to update an existing set collection by adding multiple values at once. The argument should be an iterable object.
# coll = {1, 2, 3, 4, 5}
# coll.update((10, 9, 8, 7, 6))
# print(coll)



## union()
## Syntax: set_1.union(set_2, ...., set_n)
## It is used to combine multiple set collections into a single set.
# set_1 = {1, 2, 3}
# new_set = set_1.union({3, 4, 5}, {5, 6, 7})
# print(new_set)





## intersection()
## Syntax: set_1.intersection(set_2, ..., set_n)
## It is used to find the common elements/values between multiple set collections.
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}
# set_3 = {5, 6, 7, 8, 9}
# intersect_values = set_1.intersection(set_2, set_3)
# print(intersect_values) ## {5}





## difference()
## Syntax: set_1.difference(set_2)
## It is used to return a new set collection consists of only unique values present in the first set.
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}
# print(set_1.difference(set_2)) ## {1, 2}
# print(set_2.difference(set_1)) ## {6, 7}




## symmetric_difference
## Syntax: set_1.symmetric_difference(set_2, ..., set_n)
## It is used to return a new set collection consists of only unique values present inside both the sets.
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}
# print(set_1.symmetric_difference(set_2))




## issubset()
## Syntax: subset.issubset(superset) ## Bool
## It is used to check whether the first set is the sub set of second set or not.
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(set_1.issubset(set_2))



## issuperset()
## Syntax: superset.issuperset(subset) ## Bool
## It is used to check whether the first set is the super set of second set or not.
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(set_2.issuperset(set_1))