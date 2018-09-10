Python 3.7.0b4 (v3.7.0b4:eb96c37699, May  2 2018, 19:02:22) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> files = { 'Input.txt': 'Randy',
'Code.py': 'Stan',
'Output.txt': 'Randy',
'test.py': 'Ali',
'djangoweb.py' : 'Ali'
}
>>> files ['Ali'] = 'djangoweb.py', 'test.py'
>>> files ['Stan'] = 'Code.py'
>>> files ['Randy'] = 'Output.txt', 'Input.txt'
>>> D = { 'Ali' : files['Ali'] , 'Stan' : files ['Stan'] , 'Randy' : files ['Randy'] }
>>> print (D)
{'Ali': ('djangoweb.py', 'test.py'), 'Stan': 'Code.py', 'Randy': ('Output.txt', 'Input.txt')}
>>> 
