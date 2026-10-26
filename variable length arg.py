#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
b=[2,3,4,5,6]
check(*b)
c=(3,4,5,6,7)
check(*c)
d={6,7,8,9}
check(*d)
e={"year":2026,"month":"sep"}
check(*e)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,3.4,4.2,5.3)
check1(3,4,5,2,3.2,4.4,"pooja",5+9j,True,False)'''

#kwargs(keyword variable arguments)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["mahesh","shanavaz","nivas"],"marks":[20,30,40],"status":["a","p","p"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["mahesh","shanavaz","nivas"],"marks":[20,30,40],"status":["a","p","p"]}
details(**d)'''

#both * and **
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,3.4,5.2)
final(*data)
details={"names":["bhavika","priya","sowmya"],"marks":[60,70,80]}
final(**details)
final(*data,**details)'''
