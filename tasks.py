Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[9,1,5,2,8,4,6,3,7,0]a.sort
SyntaxError: invalid syntax
a=[9,1,5,2,8,4,6,3,7,0]
a.sort()
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=[9,1,5,2,8]
b.sort()

b
[1, 2, 5, 8, 9]
>>> b.reverse()
>>> b
[9, 8, 5, 2, 1]
>>> c=[4,6,3,7,0]
>>> c.sort()
>>> c
[0, 3, 4, 6, 7]
>>> c.reverse()
>>> c
[7, 6, 4, 3, 0]
>>> print(c+b)
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> a.split()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.split()
AttributeError: 'list' object has no attribute 'split'
>>> a.slicing()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.slicing()
AttributeError: 'list' object has no attribute 'slicing'
>>> a=["code","codegnan","python"]
>>> b=str(a)
>>> b.upper()
"['CODE', 'CODEGNAN', 'PYTHON']"
