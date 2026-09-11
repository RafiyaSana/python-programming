Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=4.5
type(b)
<class 'float'>
c=[4.5]
type(c)
<class 'list'>
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
a=["ds","ai","ml"]
a.extend(["c","c++"])
a
['ds', 'ai', 'ml', 'c', 'c++']
#insert()
a=["black","white"]
a.insert(1,"blue")
a
['black', 'blue', 'white']
a=["apple","banana","grapes"]
a.index("grapes")
2
a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']
KeyboardInterrupt
KeyboardInterrupt
a=["apple","banana","grapes"]
a.index("grapes")
SyntaxError: multiple statements found while compiling a single statement
a=["hi","hello","how","are","you"]
a.pop()
'you'
a
['hi', 'hello', 'how', 'are']
a.pop("how")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.pop("how")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(2)
'how'
a
['hi', 'hello', 'are']
#remove
a.remove("hello")
a
['hi', 'are']
a=["vja","hyd","vzg","chennai"]
a.sort()
a
['chennai', 'hyd', 'vja', 'vzg']
b=[8,5,0,1,4,20,30,6]
b.sort()
b
[0, 1, 4, 5, 6, 8, 20, 30]
c=[6,9.0,"python",3+8j,True,False]
c.sort()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
a=[True,False]
a.sort()
a
[False, True]
b=[6+9j,2+4j,10+5j]
b.sort()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b.sort()
TypeError: '<' not supported between instances of 'complex' and 'complex'
a=["mango","berry","dragon"]
a.reverse()
a
['dragon', 'berry', 'mango']
a=["c","c++","java"]
>>> #len()
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> a.count("c")
1
>>> a=["python",".net","hadoop"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("sana")
>>> b
['sana']
