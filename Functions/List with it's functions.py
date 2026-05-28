Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> list1 = [ 1, 4, 90.9 ]
>>> list1
[1, 4, 90.9]
>>> list1.append([ 'HELLO', 'HI' ])
>>> list1
[1, 4, 90.9, ['HELLO', 'HI']]
>>> list1.append('python')
>>> list1
[1, 4, 90.9, ['HELLO', 'HI'], 'python']
>>> list1.append(3.27)
>>> list1
[1, 4, 90.9, ['HELLO', 'HI'], 'python', 3.27]
>>> 
>>> //insert()
SyntaxError: invalid syntax
>>> #insert()
>>> list1
[1, 4, 90.9, ['HELLO', 'HI'], 'python', 3.27]
>>> list1.insert(1, 10)
>>> list1
[1, 10, 4, 90.9, ['HELLO', 'HI'], 'python', 3.27]
>>> list1.insert(len(list1), 2000)
>>> list1
[1, 10, 4, 90.9, ['HELLO', 'HI'], 'python', 3.27, 2000]
>>> list1.insert(-7, 0.6)
>>> list1
[1, 0.6, 10, 4, 90.9, ['HELLO', 'HI'], 'python', 3.27, 2000]
>>> list1
[1, 0.6, 10, 4, 90.9, ['HELLO', 'HI'], 'python', 3.27, 2000]
>>> len(list1)
9
>>> list1.insert(-5, -1)
>>> list1
[1, 0.6, 10, 4, -1, 90.9, ['HELLO', 'HI'], 'python', 3.27, 2000]
>>> #Extend()
>>> list1.extend([ 100, 200, 300 ])
>>> list1
[1, 0.6, 10, 4, -1, 90.9, ['HELLO', 'HI'], 'python', 3.27, 2000, 100, 200, 300]
>>> #pop()
>>> list1.pop('python')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list1.pop('python')
TypeError: 'str' object cannot be interpreted as an integer
>>> list1.pop(-6)
'python'
>>> list1
[1, 0.6, 10, 4, -1, 90.9, ['HELLO', 'HI'], 3.27, 2000, 100, 200, 300]
>>> #remove()
>>> list1.remove(90.9)
>>> list1
[1, 0.6, 10, 4, -1, ['HELLO', 'HI'], 3.27, 2000, 100, 200, 300]
>>> list1.insert(-len(list1), 45)
>>> list1
[45, 1, 0.6, 10, 4, -1, ['HELLO', 'HI'], 3.27, 2000, 100, 200, 300]
>>> list1.append(100)
>>> list1
[45, 1, 0.6, 10, 4, -1, ['HELLO', 'HI'], 3.27, 2000, 100, 200, 300, 100]
>>> list1.remove(100)
>>> list1
[45, 1, 0.6, 10, 4, -1, ['HELLO', 'HI'], 3.27, 2000, 200, 300, 100]
