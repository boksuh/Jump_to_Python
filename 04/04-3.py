"""
2021-07-06
Bokyung Suh
Jump to Python
"""

f = open("newfile.txt", "w")
f.close()

f = open('test.txt', 'w')
for i in range(1, 11):
    data = "%d'th line.\n" % i
    f.write(data)
f.close()

f = open('test.txt', 'r')
line = f.readline()
print(line)
f.close()

f = open('test.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = open('test.txt', 'r')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()

f = open('test.txt', 'r')
print(f.read())
f.close()

f = open('test.txt', 'a')
for i in range(11, 20):
    data = "line #%d.\n" % i
    f.write(data)
f.close()

f = open('foo.txt', 'w')
f.write("Life is too short, you need python")
f.close()

with open('foo.txt', 'w') as f:
    f.write("Life is too short, we need python")
