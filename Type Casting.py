Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
## int -> Single Value Datatype

## int - int
int(10)
10

## int - string
str(10)
'10'

## int - float
float(10)
10.0

## int - boolean
bool(10)
True

## int- complex
complex(10)
(10+0j)

## We can't convert the single value datatype values into multi value datatype value like list, tuple, set, dict.

## float - int
int(10.2)
10

##float - float
float(10.2)
10.2

##float - string
str(10.2)
'10.2'

##float - boolean
bool(10.2)
True

##float - complex
complex(10.2)
(10.2+0j)


## string - list
list('saketh')
['s', 'a', 'k', 'e', 't', 'h']

##string - tuple
list('saketh')
['s', 'a', 'k', 'e', 't', 'h']
tuple('saketh')
('s', 'a', 'k', 'e', 't', 'h')

##string - set
set('saketh')
{'t', 'h', 'k', 'a', 'e', 's'}

## string - dictionary
dic('saketh')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dic('saketh')
NameError: name 'dic' is not defined. Did you mean: 'dir'?
dict('saketh')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict('saketh')
ValueError: dictionary update sequence element #0 has length 1; 2 is required

##string - int
int('saketh')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int('saketh')
ValueError: invalid literal for int() with base 10: 'saketh'


##complex - string
complex('saketh')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    complex('saketh')
ValueError: complex() arg is a malformed string
str(10+0j)
'(10+0j)'

##boolean - int
int(True)
1

##boolean - float
int(Flase)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
int(False)
0
float(False)
0.0

##boolean - string
str(True)
'True'

## boolean - complex
complex(False)
0j

##boolean - boolean
bool(False)
False

## string - int
str('1234')
'1234'
int('1234')
1234

##string - float
float('1234')
1234.0
##sting - boolean
bool('1234')
True

##string - complex
complex('234')
(234+0j)


## list - complex
complex([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    complex([1, 2, 3])
TypeError: complex() first argument must be a string or a number, not 'list'

##list - string
str([1, 2, 3])
'[1, 2, 3]'

##list - boolean
bool([1, 2, 3])
True

##tuple - complex
complex((1, 2, 3, 'string'))
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    complex((1, 2, 3, 'string'))
TypeError: complex() first argument must be a string or a number, not 'tuple'
##list - tuple
tuple([1, 2, 3, 'string'])
(1, 2, 3, 'string')

##list - set
set([1, 2, 'string'])
{1, 2, 'string'}

##tuple - boolean
bool((1, 3, 'string'))
True

##tuple - string
str((1, 2, 'string'))
"(1, 2, 'string')"

##tuple - list
list((1, 2, 'string'))
[1, 2, 'string']

##tuple - set
set((1, 2, 'string'))
{1, 2, 'string'}

##set - string
str({1, 2, 'string'})
"{1, 2, 'string'}"

##set - boolean
bool({1, 2, 'string'})
True

##set - list
list({1, 2.3, 'string'})
[1, 2.3, 'string']

##set - tuple
tuple({1, 2.4, 'string'})
(1, 2.4, 'string')

##set - dict
dict({('username' : 'saketh'), ('password' : '1234')})
SyntaxError: invalid syntax
dict({('username' , 'saketh'), ('password' , '1234')})
{'password': '1234', 'username': 'saketh'}
>>> 
>>> 
>>> dict( { ( 2,3 ), ( 4,5 ), ( 6,7 ) } )
{2: 3, 6: 7, 4: 5}
>>> 
>>> 
>>> ##dict - string
>>> str( { (3,4), (4,5) } )
'{(4, 5), (3, 4)}'
>>> 
>>> ##dict - boolean
>>> boolean( { (3,4), (4,5) } )
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    boolean( { (3,4), (4,5) } )
NameError: name 'boolean' is not defined
>>> bool( { (3,4), (4,5) } )
True
>>> 
>>> ## dict - list
>>> list( { (3,4), (4,5) } )
[(4, 5), (3, 4)]
>>> 
>>> ## dict - set
>>> set( { (3,4), (4,5) } )
{(4, 5), (3, 4)}
>>> 
>>> ## dict - tuple
>>> tuple( { (3,4), (4,5) } )
((4, 5), (3, 4))
>>> 
>>> tuple( { ('username', 'saketh') } )
(('username', 'saketh'),)
