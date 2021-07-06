"""
Bokyung Suh
"""

money = True
if money:
    print("ride taxi")
else:
    print("walk")

x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)

money = 2000
if money >= 3000:
    print("Taxi")
else:
    print("Walk")

card = True
if money >= 3000 or card:
    print("Taxi")
else:
    print("Walk")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("Taxi")
else:
    print("Walk")

if 'card' not in pocket:
    print("Walk")
else:
    print("Bus")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("Taxi")
else:
    if card:
        print("Taxi")
    else:
        print("Walk")

print("-----------------")

if 'money' in pocket:
    print("Taxi")
elif card:
    print("Taxi")
else:
    print("Walk")

score = 80
message = "success" if score >= 60 else "failure"
print(message)
