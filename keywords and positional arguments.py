#keywords and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="Sana"
    mailid="sana@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="himaja",mailid="h@gmail.com")
Details(id=30,name="gayathri",mailid="g@gmail.com")
Details(40,"mokshitha","m@gmail.com")
Details("vinay","v@gmail.com",50)
Details(name="rafiya",mailid="r@gmail.com",id=60)'''

#employee->name,salary,designation
'''def Details(name,salary,designation):
    print(name,salary,designation)
Details(name="name",salary="salary",designation="designation")
Details(name="sana",salary=20000,designation="Hr")
Details(30000,"senior employee","rafi")
Details("banu",40000,"developer")
Details("syed",50000,"manager")
Details(designation="asst.manager",name="shaik",salary=35000)'''

#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",1800)'''

'''def grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="ghee",price):#non-default arg follows default arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(200)'''

#bakery->cake,price,qty
'''def bakery(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.2f" %qty)
bakery("chocolate",800,500)'''

'''def bakery(cake="pineapple",price=600,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.2f"gm %qty)
bakery(600)'''

'''def bakery(cake,price=1000,qty=650):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.2f" %qty)
bakery("redvelvet")'''

'''def bakery(cake="vanilla",price,qty=500):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %.2f" %qty)
bakery(500)'''

#* arguments->* is used to unpack the elemnets
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''b=(2,3,4,5,6,7,8)
print(b)
print(*b)'''

'''c={2,3,4,5,6,7,8,9,10}
print(c)
print(*c)'''

'''d={"name":"pooja","year":2026}
print(d)
print(*d)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)#error'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)#error'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

