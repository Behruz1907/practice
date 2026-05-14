'''OPERATORS & CONDITIONS

(1) Operators
(2) Conditions
(3) Logical Operators

'''

print("==== Operators ====")
# + - > >= <= == is * /  // % += **

a = 19
b = 5


# print("a > b", a > b)
# print("a / b", a / b)
# print("a * b", a * b)


result = a // b
left = a % b
print(f"the result: {result} and left: {left}")


# a = a + 100

a += 100
print("a:", a)


print("b*2", b**2)
print("b**2", b**3)

print("="*5)


c = dict(name="Ryan", age=20)
d = dict(name="Ryan", age=20)
e = c

print("c==d", c == d)  # only value not reference
print(id(c), id(d), id(e))


print("c is d", c is d)
print("c is e", c is e)
