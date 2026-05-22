'''#add()
#syntax:coll.add(val)
##it is used to add a new value inside an existing set collection
coll={1,2,3,4,5,}
coll.add(6)
print(coll)'''


'''#clearit is used clear entire set collection
coll={1,2,3,4,5,}
coll.clear()
print(coll)'''


'''#copy()used to copy one value from the one variable other variable
coll1={1,2,3,4,5}
coll2=coll1.copy()
print(coll2)'''


'''#pop()it is used to remove the the value from the existing set collection randomly
coll={1,2,3,4,5}
coll.pop()
coll.pop()
print(coll)'''


'''#remove()used to remove a particular value from a existing set collection
coll={1,2,3,4,5}
coll.remove(3)
coll.remove(5)
print(coll)'''


'''#discard()uesd to remove a particular value from existing collection if the  value is assign it will not show any error
coll={1,2,3,4,5}
coll.discard(3)
coll.discard(5)
print(coll)'''


'''#update()uesd to update or add multiple data in to exsisting set the arrgument should iterable object
coll={1,2,3,4,4,5}
coll.update((10,9,8,7,6,))
print(coll)'''


'''#union()it is used to write all values in a single line
set_1={1,2,3}
new_set =set_1.union({3,4,5} ,{5,6,7})
print(new_set)'''


'''#intersection()it is used to find the common elements/values between mutiple set collections
set_1={1,2,3,4,5}
set_2={3,4,5,6,7}
set_3={5,6,7,8,9}
intersect_values=set_1.intersection(set_2,set_3)
print(intersect_values)'''


'''#differences() it is used to return a new set collection consists of only unique values present in the first set
set_1={1,2,3,4,5}
set_2={3,4,5,6,7}
print(set_1.difference(set_2))
print(set_2.difference(set_1))'''


'''#symmentric_difference()it is used return a new set of collection consist of unique values present inside both the sets
set_1={1,2,3,4,5}
set_2={3,4,5,6,7}
print(set_1.symmetric_difference(set_2))'''


'''#issubset()it is used to check wheather the first set is the sub set of second set or  not
set_1={1,2,3}
set_2={1,2,3,4,5}
print(set_1.issubset(set_1))'''


'''#issuperset()it is used to check whether the first set is the super set of second set or not
set_1={1,2,3,4,5}
set_2={1,2,3,2,5}
print(set_2.issuperset(set_1))'''







    


