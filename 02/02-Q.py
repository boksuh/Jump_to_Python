"""
Bokyung Suh
"""

# 1
korean = 80
eng = 75
math = 55
avg = (math + eng + korean) / 3
print(avg)

# 2
if 13 % 2 == 0:
    print("even")
else:
    print("odd")

# 3
pin = "881120-1068234"
yyymmdd = pin[:6]
num = pin[7:]
print(yyymmdd, num)

# 4
print(pin[7])

# 5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# 7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# 8
a = (1, 2, 3)
a = a+(4,)
print(a)

# 10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12
a = b = [1, 2, 3]
a[1] = 4
print(b)