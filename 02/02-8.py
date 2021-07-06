"""
Bokyung Suh
"""
from copy import copy

a = 1
b = "python"
c = [1, 2, 3]

print(id(a))

d = c
print(id(c))
print(id(d))
print(d is c)

c[1] = 4

print(c)
print(d)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = copy(a)
print(b)
print(a)

a, b = ('python', 'life')
print(a)

(a, b) = 'python', 'life'

[a, b] = ['python', 'life']

a = b = 'python'

a, b = 3, 5
a, b = b, a
print(a, b)
