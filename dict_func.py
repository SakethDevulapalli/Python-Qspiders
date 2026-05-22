## clear()
## copy()
## get()
## keys()
## values()
## items()
## pop()
## popitem()



## clear()
## Syntax: coll.clear()
## It is used to remove all the key-value pairs from a dictionary and make the dictionary empty.
# user = {
#     'username': 'user@123',
#     'password': '****'
# }

# user.clear()
# print(user)




## copy()
## Syntax: dest_var = source_var.copy()
## It is used to perform shallow copy.




## get()
## Syntax: coll.get(key)
## It is used to access the value of a particular key.
# user = {
#     'username': 'user@123',
#     'password': '****'
# }
# print(user.get('username'))
# print(user.get('password'))



## pop()
## Syntax: coll.pop(key)
## It is used to remove a particular key-value pair from an existing dictionary.
# user = {
#     'username': 'user@123',
#     'password': '****',
#     'is_logged_in': True
# }
# print(user)
# print(user.pop('is_logged_in')) ## value
# print(user)




## popitem()
## Syntax: coll.popitem()
## It is used to remove key-value pair from a dictionary from the end and returns it in the form of tuple.
# user = {
#     'username': 'user@123',
#     'password': '****',
#     'is_logged_in': True
# }
# print(user.popitem())
# print(user.popitem())
# print(user.popitem())
# print(user)




## keys()
## Syntax: coll.keys()
## It is used to display all the key names present inside the dictionary in the form of dict_keys.
# user = {
#     'username': 'user@123',
#     'password': '****',
#     'is_logged_in': True
# }
# print(user.keys())
# print(list(user.keys()))
# print(tuple(user.keys()))





## values()
## Syntax: coll.values()
## It is used to display all the values present inside the dictionary in the form of dict_values.
# user = {
#     'username': 'user@123',
#     'password': '****',
#     'is_logged_in': True
# }
# print(user.values())
# print(list(user.values()))
# print(tuple(user.values()))




## items()
## Syntax: coll.items()
## It is used to return all the key-value pairs from the dictionary in the form of tuple.
user = {
    'username': 'user@123',
    'password': '****',
    'is_logged_in': True
}
print(user.items())
print(list(user.items()))
print(tuple(user.items()))