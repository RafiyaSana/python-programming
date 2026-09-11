Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"sana","city":"vja"}
>>> print(a)
{'name': 'sana', 'city': 'vja'}
>>> type(a)
<class 'dict'>
>>> b={"name","sana"}
>>> type(b)
<class 'set'>
>>> a={"year":2026,"month":"sep","date":9}
>>> a.keys()
dict_keys(['year', 'month', 'date'])
>>> a.values()
dict_values([2026, 'sep', 9])
>>> a.items()
dict_items([('year', 2026), ('month', 'sep'), ('date', 9)])
>>> a["year"]
2026
>>> a[2026]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[2026]
KeyError: 2026
>>> a.get("year")
2026
a={"name":"sana","city":"vja"}
a.update({"mailid":"rafiyasana@gmail.com"})
a
{'name': 'sana', 'city': 'vja', 'mailid': 'rafiyasana@gmail.com'}
a.update({"year":2026,"time":3})
a
{'name': 'sana', 'city': 'vja', 'mailid': 'rafiyasana@gmail.com', 'year': 2026, 'time': 3}
a.update({"year":2026},{"time":3})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.update({"year":2026},{"time":3})
TypeError: update expected at most 1 argument, got 2
a={"hour":3,"min":10}
a.setdefault("sec",4)
4
a
{'hour': 3, 'min': 10, 'sec': 4}
a={"week":"wed","date":9}
a.pop()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("week")
'wed'
a
{'date': 9}
a={"country":"india","state":"ap"}
a.popitem()
('state', 'ap')
a
{'country': 'india'}
a={"name":"sana","course":"python","duration":100}
a.copy()
{'name': 'sana', 'course': 'python', 'duration': 100}
len(a)
3
a.count("name")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a.index("course")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.index("course")
AttributeError: 'dict' object has no attribute 'index'
a={"name":"sana","year":2026,"name":"sana"}
print(a)
{'name': 'sana', 'year': 2026}
a={"name":"sana","year":2026,"name":"rafiya"}
print(a)
{'name': 'rafiya', 'year': 2026}
a={"name":"sana","year":2026,"name1":"rafiya"}
print(a)
{'name': 'sana', 'year': 2026, 'name1': 'rafiya'}
a={"idnos":[10,20,30],"names":["rafiya","sana"],"places":["vja","hyd","vzg"]}
print(a)
{'idnos': [10, 20, 30], 'names': ['rafiya', 'sana'], 'places': ['vja', 'hyd', 'vzg']}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'places'])
a.values()
dict_values([[10, 20, 30], ['rafiya', 'sana'], ['vja', 'hyd', 'vzg']])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['rafiya', 'sana']), ('places', ['vja', 'hyd', 'vzg'])])
