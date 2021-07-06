"""
Bokyung Suh
"""

dic = {'name': 'pey', 'phone': '01051776487', 'birth': '1025'}

a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)

grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

print(dic.keys())

for k in dic.keys():
    print(k)

print(list(dic.keys()))

print(dic.values())

print(dic.items())

print(dic.get('name'))
print(dic.get('phone'))

print(dic.get('foo', 'bar'))

print('name' in a)

print('email' in a)

