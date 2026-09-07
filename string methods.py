Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #len()
>>> a="python"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=''
>>> len(c)
0
>>> c=' '
>>> len(c)
1
>>> #count
>>> a="twinkle twinkle little star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("t")
5
a.count("l")
4
a.count("")
28
a.count(" ")
3
#find a string
a="python"
a[1]
'y'
a.find("y")
1
a.find("o")
4
#escape sequences
#n->new line
#\t->tab space
a="idno\nname\nmobileno\nmailid\nbranch\tcollege"
print(a)
idno
name
mobileno
mailid
branch	college
b="idno:14\nname:sana\tmobileno:0123456789\nmailno:39\nbranch:cse\tcollege:nri
SyntaxError: unterminated string literal (detected at line 1)
b="idno:14\nname:sana\tmobileno:0123456789\nmailno:39\nbranch:cse\tcollege:nri"
print(b)
idno:14
name:sana	mobileno:0123456789
mailno:39
branch:cse	college:nri
