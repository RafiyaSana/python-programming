Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[1]
'i'
a[5]
'a'
a[2]
'j'
a[0],a[1]
('v', 'i')
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[4]
' '
a[7]
' '
a[1]+a[4]+a[7]
'   '
a="i am learning python fullstack"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[29]
'fullstack'
>>> a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'learning'
>>> a[2]+a[3]
'am'
>>> a="time is very precious"
>>> a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'precious'
>>> a[-13]+a[-12]+a[-11]+a[-10]
'very'
>>> a[-21]+[-20]+a[-19]+a[-18]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[-21]+[-20]+a[-19]+a[-18]
TypeError: can only concatenate str (not "list") to str
>>> a[-21]+a[-20]+a[-19]+a[-18]
'time'
>>> a="codegnan it solution"
>>> a[-20]+a[-19]+a[-18]+a[-17]
'code'
>>> a[-16]+a[-15]+a[-14]+a[-13]
'gnan'
>>> a[-20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]+a[-13]
'codegnan'
>>> a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solution'
