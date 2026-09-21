#if-conditions by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")'''

'''a=40
b=60
if a>b:
    print("less")'''

'''a=50
b=80
if b>a:
    print("Greater")'''

'''a=5
b=9
if a<=b:
    print("Greater")'''

'''a=11
b=13
if b>=a:
    print("Greater")'''

'''a=7
b=8
if a!=b:
    print("not equal")'''

'''a=5
b=5
if a==b:
    print("equal")'''

'''a="python"
if a=="python":
    print("true")'''

'''a="java"
if a!="python":
    print("false")'''
    
'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a>30:
    print("true")'''

#if-condition by using logical operators
#and,or,not
'''a=4
b=8
if a<b and b>a:
    print("less")'''

'''a=6
b=9
if a<=b and b>=a:
    print("less")'''

'''a=7
b=10
if a!=b and b==a:
    print("less")'''

'''a=12
b=14
if a<b or b>a:
    print("true")'''

'''a=15
b=20
if a<=b or b>=a:
    print("true")'''

'''a=10
b=20
if a!=b or b==a:
    print("true")'''

'''a=3
b=5
if not a<b:
    print("true")'''

'''a=3
b=5
if not a>b:
    print("true")'''

'''a=3
b=5
if not a<b and b>a:
    print("true")'''

#if-condition by using identify operators
#is,is not
'''a=10
if type(a) is int:
    print("it is int")'''

'''a=7
if type(a) is not int:
    print("false")'''

'''a=10.5
if type(a) is not int:
    print("its not int")'''

'''a=int(input("a value"))
if type(a) is int:
    print("true")'''

#if-condition by using membership operators
#in,not in
'''a=[2,3,4,5,6,7,8,9,10]
if 5 in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 10 not in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 15 not in a:
    print("true")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")'''#error

'''a=[2,3,4,5,6,7,8,9,10]
b=int(input("enter the value"))
if b in a:
    print("true")'''

#if-else conditions by using comparision operators
'''a=5
b=9
if a<b:
    print("less")
else:
    print("false")'''

'''a=15
b=20
if a>b:
    print("less")
else:
    print("false")'''

'''a=15
b=30
if a!=b:
    print("true")
else:
    print("false")'''

'''a=15
b=15
if a==b:
    print("true")
else:
    print("false")'''

#if-else condition opeartors
#and,or,not
'''a=10
b=12
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=40
b=10
if a<=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=50
b=20
if a!=b and b==a:
    print("true")
else:
    print("false")'''

'''a=10
b=12
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=20
b=15
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=20
b=40
if a!=b or b==a:
    print("true")
else:
    print("false")'''

'''a=3
b=5
if not a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=15
b=13
if not a<=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=20
b=20
if not a!=b and b==a:
    print("true")
else:
    print("false")'''

#if-else condition identify operators 
#is,is not
'''a=10
if type(a) is int:
    print("is int")
else:
    print("not int")'''

'''a=2.5
if type(a) is int:
    print("true")
else:
    print("false")'''

#if-else condition membership operators
#in,not in
'''a=[2,3,4,5,6,7,8,9,10]
if 5 in a:
    print("true")
else:
    print("false")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 25 not in a:
    print("true")
else:
    print("false")'''

#if-elif-else conditions by using comparision operators
'''a=2
b=4
if a<b:
    print("less")
elif a>b:
    print("greater")
else:
    print("true")'''

'''a=5
b=6
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=9
b=12
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''

#nested-elif
'''a=3
b=5
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("true")'''

#if-elif-if conditional statements by logical operators
'''a=4
b=8
if a<b and b>a:
    print("less")
elif a>=b or b<=a:
    print("greater")
else:
    print("true")'''

#if-elif-if conditional statements by identify operators
'''a=2.4
if type(a) is int:
    print("is int")
elif type(a) is not int:
    print("is not int")
else:
    print("false")'''

#if-elif-if conditional statements by membership operators
'''a=[2,3,4,5,6,7,8,9,10]
if 20 in a:
    print("true")
elif 15 not in a:
    print("not in")
else:
    print("false")'''

#multiple if conditions by using comparision operators
'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=5
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''

'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
else a!=b:
    print("not equal")'''

#multiple if conditional statements by logical operators
'''a=20
b=10
if a<b and b>a:
    print("less")
if a>=b or b<=a:
    print("greater")
if a!=b and a==b:
    print("true")'''

#multiple if conditional statements by identify operators
'''a=2
b=4.5
if type(a) is int:
    print("is int")
if type(b) is not int:
    print("is not int")'''

#multiple if conditional statements by membership operators
'''a=[2,3,4,5,6,7,8,9,10]
if 20 in a:
    print("true")
if 15 not in a:
    print("not in")
if 5 in a:
    print("false")'''

#nested-if
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a>b:
    print("less")
if b>a:
    print("greater")'''

'''a=6
b=12
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("equal")
else:
    print("true")'''
    
'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a>b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")'''

'''a=5
b=15
if a>b and b>a:
    print("less")
    if a<=b or a>=b:
        print("greater")
    elif a!=b and a==b:
        print("equal")
else:
    print("true")'''

'''a=10
b=2.8
if type(a) is int:
    print("is int")
    if type(b)is not int:
        print("is not int")
else:
    print("true")'''

a=[1,2,3,4,5,6,7,8]
if 5 in a:
    print("in a")
    if 2 not in a:
        print("high")
else:
    print("true")
