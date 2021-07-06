# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:36:18 2021

@author: Bokyung Suh

점프 투 파이썬
"""

print("{0:<10}".format("hi"))

print("{0:>10}".format("hi"))

print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))

print("{0:!<10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y))

print("{0:10.4f}".format(y))

print("{{ and }}".format())

name = "gildong"
age = 30
print(f'my name is {name}. my age is {age}')

print(f'I am {age+1} next year.')

d = {'name': 'gildong', 'age': 30}
print(f'my name is {d["name"]}. I am {d["age"]}.')

print(f'{"hi":<10}')

print(f'{"hi":>10}')

print(f'{"hi":^10}')

print(f'{"hi":=^10}')

print(f'{"hi":!<10}')

print(f'{y:0.4f}')

print(f'{y:10.4f}')

print(f'{{and}}')

print(f'{"python":!^12}')

a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

a = "Life is too short"
print(a.index('t'))

print(",".join('abcd'))

print(",".join(['a', 'b', 'c', 'd']))

a = "hi"
print(a.upper())

a = "HI"
print(a.lower())

a = " hi "
print(a.lstrip())

a = " hi "
print(a.rstrip())

a = "   hi    "
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))