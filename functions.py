#functions
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#//,**,%
'''def calculate(a,b):
    print("the intdiv is",a//b)
    print("the pow is",a**b)
    print("the mod is",a%b)
calculate(10,20)
calculate(2,5)
calculate(5,6)'''

'''while True:
    def add():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    add()'''

'''def add():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
        add()
add()'''

'''def fullname():
    fname=input("fname:")
    lname=input("lname:")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return a*b
print(mul(5,2))'''

#print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    #return(d)
    #return(e)
    return c,d,e
print(cal(5,4))'''

#method1
'''while True:
    def cal():
        a=int(input("a value:"))
        b=int(input("b vale:"))
        option=int(input(choose the option
                         1.add
                         2.sub
                         3.mul:))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
    cal()'''

#method2
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value:"))
    b=int(input("b vale:"))
    option=int(input(choose the option
                         1.add
                         2.sub
                         3.mul:))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''
    
#task
#splitbill
'''def splitbill():
    a=int(input("enter the total members:"))
    b=int(input("enter the total amount:"))
    print("perhead bill is",b//a)
splitbill()'''

'''def splitbill():
    a=int(input("enter the total members:"))
    b=int(input("enter the total amount:"))
    c=b//a
    print("perhead bill is {}".format(c))#formatmethod
    print(f"perhead bill is {c}")#fstrmethod
splitbill()'''
