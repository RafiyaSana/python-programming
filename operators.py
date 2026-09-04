Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=6
print(a+b)
8
print(a-b)
-4
print(a*b)
12
print(a//b)
0
print(a/b)
0.3333333333333333
print(a%b)
2
print(a**b)
64
#assignment
a=3
b=6
a+=b
a
9
a-=b
a
3
a*=b
a
18
a//=b
a
3
a/=b
a
0.5
a%=b
a
0.5
a**=b
a
0.015625
b+=b
b
12
b+=a
b
12.015625
b-=a
b
12.0
b*=a
b
0.1875
b//=a
b
12.0
b/=a
b
768.0
b%=a
b
0.0
b**=a
b
0.0
#comparision
a=8
b=10
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
a>=b
False
b<=a
False
b>=a
True
#logical
a=5
b=10
a<b and b>a
True
a>b and b<a
False
a>b and b>a
False
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b<=a
True
a>=b or b>=a
True
a!=b or a==b
True
not False
True
not True
False
#identify
#or identity
a=4
type (a) is int
True
type(a) is not int
False
b=2.6
type(b)is float
True
type(b)is not float
False
>>> type(b)is int
False
>>> type(b)is not int
True
>>> #membership
>>> a=2,3,4,5,6,7,8,9
>>> 6 in a
True
>>> 9 in a
True
>>> 10 in a
False
>>> 10 not in a
True
>>> #bitwise
>>> a=2
>>> b=6
>>> a&b
2
>>> bin(2)
'0b10'
>>> bin(6)
'0b110'
>>> a|b
6
>>> a=4
>>> ~a
-5
b=-5
~b
4
a=3
b=5
a^b
6
a=3
a<<3
24
a=5
a>>2
1
a=7
a>>3
0
a>>2
1
