Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> user = {
...     'username': 'user123',
...     'password': '9876',
...     'is_logged_in': 'True',
...     'login_devices': [ 'Windows', 'Android' ]
... }
>>> user
{'username': 'user123', 'password': '9876', 'is_logged_in': 'True', 'login_devices': ['Windows', 'Android']}
>>> user['username']
'user123'
>>> user['password']
'9876'
>>> user['is_logged_in']
'True'
>>> user['login_deivce']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    user['login_deivce']
KeyError: 'login_deivce'
>>> user['login_deivces']
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    user['login_deivces']
KeyError: 'login_deivces'
>>> user['login_devices']
['Windows', 'Android']
>>> user['login_devices'][1]
'Android'
>>> user['login_devices'][0]
'Windows'
>>> user['location'] = 'India'
>>> user
{'username': 'user123', 'password': '9876', 'is_logged_in': 'True', 'login_devices': ['Windows', 'Android'], 'location': 'India'}
>>> user['email'] = 'user@gmail.com'
>>> user
{'username': 'user123', 'password': '9876', 'is_logged_in': 'True', 'login_devices': ['Windows', 'Android'], 'location': 'India', 'email': 'user@gmail.com'}
