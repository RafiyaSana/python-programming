Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[4:7]
'gna'
a[:4]
'code'
a[4:]
'gnan'
a="work until you succeed"
a[4:10]
' until'
a[5:10]
'until'
a[15:21]
'succee'
a[15:22]
'succeed'
a[11:14]
'you'
a[0:4]
'work'
a="vijayawada is a royal city"
a[22:26]
'city'
a[16:21]
'royal'
a[0:10]
'vijayawada'
a[11:13]
'is'
a="happy teachers day"
a[-3:-0]
''
a[-4:]
' day'
a[-3:]
'day'
a[-18:-13]
'happy'
a[-12:-4]
'teachers'
a="vizag is a city of destiny"
a[-26:-21]
'vizag'
a[-15:-11]
'city'
a[-7:]
'destiny'
#striding
a=
SyntaxError: invalid syntax
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a="machine learning"
a[::3]
'mheeng'
a[: :3]
'mheeng'
a[::5]
'mnag'
a[::2]
'mcielann'
m[::9]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    m[::9]
NameError: name 'm' is not defined
a[::9]
'me'
a[3:11]
'hine lea'
a[5:]
'ne learning'
a[:7]
'machine'
a="cloud computing"
a[1:7:2]
'lu '
a[2:13:3]
'o mt'
a[4:14:5]
'dp'
>>> a[3:12:6]
'up'
>>> a="python course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-5]
'uo'
>>> a[-6:-12:-2]
'cnh'
>>> ex:
...     
SyntaxError: invalid syntax
>>> a="python course"
>>> a[7:3:2]
''
>>> a[3:7:2]
'hn'
>>> a[-9:-5:-2]
''
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
