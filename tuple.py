Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(5,7.8,"sana",4+9j,True,False)
>>> print(a)
(5, 7.8, 'sana', (4+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.count(4+9j)
1
>>> a.index(False)
5
>>> #sets{}
>>> a={7,4.5,"python",5+9j,True,False}
>>> print(a)
{False, True, (5+9j), 4.5, 7, 'python'}
>>> type(a)
<class 'set'>
>>> b={7,9,4,0.1,4,7,9}
>>> print(b)
{0.1, 9, 4, 7}
>>> b={7,9,4,0,1,4,7,9}
>>> print(b)
{0, 1, 4, 7, 9}
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a={4,5,6,7,8,9}
b={7,8,9}
b.issubset(a)
True
a.issubset(b)
False
a={6,7,8,9,10,11,12}
b={10,11,12}
a.issuperset(b)
True
b.issuperset(a)
False
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a={10,11,12,13,14,15}
b={14,15,16,17}
a.intersection(b)
{14, 15}
a={2,3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a={6,7,8,9,10,11}
b={2,3,4,5,6,7,8}
a.difference(b)
{9, 10, 11}
b.difference(a)
{2, 3, 4, 5}
a={7,8,9,10,11,12,13}
b={10,11,12,13,14,15}
a.symmetric_difference(b)
{7, 8, 9, 14, 15}
a=
SyntaxError: invalid syntax
a={3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.difference_update(b)
a
{3}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9, 10}
a={3,4,5,6,7,8}
b={1,3,6,7,8,9,10}
a.intersection_update(b)
a
{8, 3, 6, 7}
b.intersection_update(a)
b
{8, 3, 6, 7}
a={6,7,8,9,10,11,12}
b={10,11,12,13,14,15}
a.symmetric_difference_update(b)
a
{6, 7, 8, 9, 13, 14, 15}
b.symmetric_difference_update(a)
b
{6, 7, 8, 9, 10, 11, 12}
a={10,20,30,40,50}
a.pop()
50
a
{20, 40, 10, 30}
a.pop()
20
a.remove(10)
a
{40, 30}
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
a={4,5,6,7,8,9}
a.discard(8)
a
{4, 5, 6, 7, 9}
a.copy()
{4, 5, 6, 7, 9}
a
{4, 5, 6, 7, 9}
b=a.copy()
b
{4, 5, 6, 7, 9}
a={3,4,5,6,7}
a.clear()
a
set()
b=set()
b.add(50)
b
{50}
a={5,6,7,8}
len(a)
4
a.index(4)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
a.count(5)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
a={3,4,5,6,7,8}
b={2,3,4,6,7}
a.isdisjoint(b)
False
a={6,7,8,9}
b={1,2,3,4}
a.isdisjoint(b)
True
