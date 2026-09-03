Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types
a=7
type(a)
<class 'int'>
b=6.7
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d='course'
type(d)
<class 'str'>
e="course"
type(e)
<class 'str'>
f='''codegnan'''
type(f)
<class 'str'>
g=6+9j
type(g)
<class 'complex'>
h=4j+6
type(h)
<class 'complex'>
i=8j
type(i)
<class 'complex'>
j=5j+8j
type(j)
<class 'complex'>
k=6+5i
SyntaxError: invalid decimal literal
l=True
type(l)
<class 'bool'>
m=False
type(m)
<class 'bool'>
#data type conversions
#int
int(8)
8
int(8.9)
8
int('python')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int('python')
ValueError: invalid literal for int() with base 10: 'python'
int(2+4j)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(2+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(4)
4.0
float(2.5)
2.5
float('python')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float('python')
ValueError: could not convert string to float: 'python'
float(2+4j)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(2+4j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(false)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
float(False)
0.0
#str
str(5)
'5'
str(2.6)
'2.6'
str('python')
'python'
str(2+4j)
'(2+4j)'
str(True)
'True'
str(False)
'False'
#complex
complex(8)
(8+0j)
>>> complex(2.5)
(2.5+0j)
>>> complex('python')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex('python')
ValueError: complex() arg is a malformed string
>>> complex(2+4j)
(2+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(8)
True
>>> bool(2.5)
True
>>> bool('python')
True
>>> bool(2+4j)
True
>>> bool(True)
True
>>> bool(False)
False
