Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #replace
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b="python java"
>>> b.replace("java","c")
'python c'
>>> #upper
>>> a="python"
>>> a.upper()
'PYTHON'
>>> b="CODE"
>>> b.lower
<built-in method lower of str object at 0x000002253E46E0D0>
>>> b.lower()
'code'
>>> c="java"
>>> c.upper(0)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c.upper(0)
TypeError: str.upper() takes no arguments (1 given)
>>> #capitalize
>>> c.capitalize()
'Java'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
e.capitalize()
'I am in class'
a="hello world"
a.startswith("h")
True
a.endswith("d")
True
b="helloworld"
b.isalpha()
True
a.isdigit()
False
b=13456
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="1408"
b.isdigit()
True
a.isalnum()
False
c="java"
c.alnum()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
c.isalnum()
True
d="sana08"
d.isalnum()
True
#strip()
#lstrip(),rstrip()
a="         rafiya       "
a.strip()
'rafiya'
a.lstrip()
'rafiya       '
a.rstrip()
'         rafiya'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="sana"
lname="sd"
print(fname+lname)
sanasd
print(fname+" "+lname)
sana sd
print(fname.title()+lname.title())
SanaSd
print(fname.title()+" "+lname.title())
Sana Sd
print((fname+" "+lname).title())
Sana Sd
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learing python"
b.split()
['i', 'am', 'learing', 'python']
#join()
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
" ".join(b)
'vja hyd vzg'
"k".join(b)
'vjakhydkvzg'
#formating
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
print("the sum is,a+b")
the sum is,a+b
city="vja"
print("city is",city)
city is vja
#format()
a="motu"
b="pathlu"
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello {} hello {}".format(a,b))
hello motu hello pathlu
#fstring()
a="virat"
b="kohli"
print(f"hello {a}{b}")
hello viratkohli
print(f"hello {a} {b}")
hello virat kohli
print(f"hello {a} hello {b}")
hello virat hello kohli
a="rafiya"
b="sana"
print("hello {}{}".format(a,b))
hello rafiyasana
print("hello {} {}".format(a,b))
hello rafiya sana
print("hello {} hello {}".format(a,b))
hello rafiya hello sana
fname="rafiya"
lname="sana"
print(fname+lname)
rafiyasana
print(fname+" "+lname)
rafiya sana
print(f"hello {fname} {lname}")
hello rafiya sana
print(f"hello {fname} hello{lname})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {fname} hello{lname}")
      
hello rafiya hellosana
print(f"hello {fname} hello {lname}")
      
hello rafiya hello sana
print("full name is {} {}".format(fname,lname))
      
full name is rafiya sana
print("full name is {}".format(fname,lname))
      
full name is rafiya
print("full name is {}".format(fname+lname))
      
full name is rafiyasana
