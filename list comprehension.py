#list comprehension
#Every list comprehension
'''a=["python","java","dsa"]'''
#print(a.upper())error
'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

'''b=["apple","mango"]
c=[i.capitalize() for i in b]
print(c)'''

'''a=[1,2,3,5,6,8,12,13]
b=[i**2 for i in a]
b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)'''

'''a=[i for i in range(21)]
print(a)'''

'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i**2 for i in range(31) if i%2==0]
print(a)'''

'''a=["grapes","berry","mango","kiwi","dragon","apple"]
b=[i for i in a if "a" in i]
print(b)'''

'''a=["grapes","berry","mango","kiwi","dragon","apple"]
b=[i for i in a if "a" not in i]
print(b)'''

'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]'''
#[6,6,6,6,6]answer
'''c=[a[i]+b[i] for i in range(len(a))]
print(c)'''
'''c=[a[i]+b[i] for i in range(5)]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''
