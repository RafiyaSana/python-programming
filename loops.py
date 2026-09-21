#loops(for,while,range,break,continue,pass
#for loop()
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(6,7,8,9,10)
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={4,5,6,7,8,9,10}
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={"year":2026,"month":"sep","date":16}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[4.5,6.7,8.9]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=["python","c","java"]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[4+7j,7+2j]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[True,False]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[3,4.5,"hello",4+7j,True,False]
for i in a:
    print(i)
    print(type(i))'''

#task
'''a=["apple","banana","grapes"]
b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#while loop
'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=20
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>1:
    a=a-1
    print(a)'''

'''a=15
while a>2:
    print(a)
    a=a-1'''

'''a=20
while a>1:
    a=a-1
print(a)'''

'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''
    
'''a=5
while a<15:
    print(a)
    a+=1'''

'''while True:
    age=int(input("enter the age:"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote:")'''

'''age=int(input("enter the age:"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")'''

#range(start-stop-step)
#def->
'''for i in range(10):
    print(i)'''

'''for i in range(15,30):
    print(i)'''

#task
'''for i in range(0,20,2):
    print(i,end=",")'''

'''for i in range(5,50,2):
    print(i,end=",")'''

'''for i in range(3,30,3):
    print(i,end=",")'''

#student marks
'''while True:
    marks=int(input("enter marks:"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(61,71):
        print("Grade-D")
    elif marks in range(51,61):
        print("Grade-E")
    else:
        print("Fail prepare well......")'''

'''while True:
    students=int(input("enter total  no.of students:"))
    p=0
    a=0
    for i in range(1,students+1):
        attendence=input(f"students {i} (p/a)")
        if attendence=="p":
            p+=1
        elif attendence=="a":
            a+=1
    print("Attendence Tracker........")
    print("Total no.of students:",students)
    print("Total no.of presenties:",p)
    print("Total no.of absenties:",a)'''

#break
'''a=10
while a>1:
    print(a)
    a=a-1'''
    
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==4:
        break
    print(a)'''

'''for i in range(10):
    if i==8:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print(a)'''#error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    a=a-1
    print(a)
    if a==12:
        continue'''

'''a=20
while a>5:
    a=a-1
    if a==12:
        continue
    print(a)'''

'''for i in range(15):
    if i==10:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#pass
'''a=5
while a>1:
    print(a)
    a=a-1
    if a==2:
        pass'''

'''for i in range(25):
    if i==10:
        pass
    print(i)'''
