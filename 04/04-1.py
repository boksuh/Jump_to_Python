"""
2021-07-06
Bokyung Suh
Jump to Python
"""


def add(a, b):
    return a + b


print(add(1, 2))


def say():
    return "HI"


print(say())


def add(a, b):
    print("Sum of %d and %d is %d" % (a, b, a + b))


add(3, 4)


def say():
    print("HI")


say()


def add(a, b):
    return a + b


result1 = add(a=3, b=7)
print(result1)


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


result2 = add_many(1, 2, 3)
print(result2)

result2 = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result2)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))


def add_and_mul(a, b):
    return a + b, a * b


res = add_and_mul(3, 4)
print(res)

res1, res2 = add_and_mul(3, 4)
print(res1, res2)


def say_myself(name, old, man=True):
    print("my name is %s" % name)
    print("my age is %d" % old)
    if man:
        print("I am man")
    else:
        print("I am woman")


say_myself("Bokyung", 25)
say_myself("Gaye", 22, False)

a = 1


def vartest():
    global a
    a = a + 1


vartest()
print(a)

add = lambda a1, b: a1 + b
res = add(3, 4)
print(res)
