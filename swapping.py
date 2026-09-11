#swapping of two variables
#without temp
'''a=10
b=20
a=b,b=a
print(a)
print(b)'''

#with temp
'''a=10
b=20
temp=a
a=b
b=temp
print("a value is",a)
print("b value is",b)'''

#with arthematic
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("a value is",a)
print("b value is",b)'''

#with
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d",(a,b))
print("after swapping a=%.2f,b=%.2f",(a,b))'''

#using string
'''a="python"
b="course"
temp=a
a=b
b=temp
print("a is",a)
print("b is",b)'''

'''a="python"
b="course"
a=b,b=a
print("a is",a)
print("b is",b)'''

a="python"
b="course"
a=a+b
b=a-b
a=a-b
print("a is",a)
print("b is",b)
