"""
Bokyung Suh
"""

# 1
a = "Life is too short, you need python"
if "shirt" not in a: print("shirt")


# 2
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

# 3
i = 0
while True:
    i += 1
    if i > 5: break
    print("*"*i)

# 4
for i in range(1, 101):
    print(i)

# 5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / 10
print(average)

# 6
numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers if num % 2 != 0]
print(result)