# Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
# Enter "help" below or click "Help" above for more information.
list_1 = [ 1, 2, 3, 4, 5 ]
list_1
[1, 2, 3, 4, 5]

#print [ 2, 3, 4 ]
#si = 1; ei = 4; updation = +1
#var_name[ si : ei +-1 : updation ]

list_1[ 1 : 4 : 1 ]
[2, 3, 4]
# or
list_1[ 1 : 4 ]
[2, 3, 4]

#print [ 1, 2, 3, 4, 5 ]
list_1[ 0 : 5 ]
[1, 2, 3, 4, 5]
#print [ 3, 4 ]
list_1[ 1 : 4 ]
[2, 3, 4]
list_1[ 2 : 4 ]
[3, 4]

#print[ 1, 2, 3, 4, 5 ]
list_1[ : : ]
[1, 2, 3, 4, 5]
list_1[ : ]
[1, 2, 3, 4, 5]
list[ : : 1 ]
list[slice(None, None, 1)]


#Using string
str = 'PYTHON'

#print PTO from the PYTHON
#updation is used for gaps in between the char or num

str[ 0 : 5 : 2 ]
'PTO'
#or
str[ : 5 : 2 ]
'PTO'

#print 'NOHTYP'
str[ 5 :  : -1 ]
'NOHTYP'
str[ : : -1 ]
'NOHTYP'


#Print 'SARIKA'
str = 'SARIKA'
str[ : : ]
'SARIKA'

#print 'AKIRAS'
str[ 5 : : -1 ]
'AKIRAS'


# Tuple
tpl
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    tpl
NameError: name 'tpl' is not defined
-
tpl_1( 2, 4, 6, 8, 10 )
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    tpl_1( 2, 4, 6, 8, 10 )
NameError: name 'tpl_1' is not defined
tpl_1 = ( 2, 4, 6, 8, 10 )
tpl_1
(2, 4, 6, 8, 10)


#print (3)
tpl_1[ 2 : 3 : 1 ]
(6,)
#print (8)
tpl_1[ 3 : 4 ]
(8,)
#or
tpl_1[ 3 : 4 : 1 ]
(8,)


## Slicing using negative indexing
str = 'PROGRAM'

#print 'OGR'
str[ -5 : -2 : 1 ]
'OGR'
#or
str[ -5 : -2 ]
'OGR'
#print 'OG'
str[ -5 : -3 ]
'OG'


#print 'GO'
>>> str[ -4 : -6 : -1 ]
'GO'
>>> str[ -4 : -6  ]
''
>>> str[ -4 : -6 :  ]
''
>>> str[ -4 : -6 : 1 ]
''
>>> str[ -4 : -6 : -1 ]
'GO'
>>> 
>>> 
>>> #print 'MARG'
>>> str[ -5 : : -1 ]
'ORP'
>>> str[ -5 : -1 : -1 ]
''
>>> str[ -1 : -5 : -1 ]
'MARG'
>>> str[ : -5 : -1 ]
'MARG'
>>> str[ : : -1 ]
'MARGORP'
>>> 
>>> 
>>> list_1 = [ 1, 2, 3, 4, 5 ]
>>> 
>>> #[ 4, 2 ]
>>> list_1[ -2 : : -2 ]
[4, 2]
>>> #or
>>> list_1[ -2 : -5 : -2 ]
[4, 2]
