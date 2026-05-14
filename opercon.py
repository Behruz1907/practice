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


print("==== CONDITION ====")  # always check truthy or falsy

x = 45

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("==== Logical Operators ====")

age = 15
# person = None
if age > 16:
    person = "adult"
else:
    person = "child"


print("person:", person)


# Ternary
person = "adult" if age > 18 else "minor"
print("person:", person)


is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here, do you want to be a student?")
elif is_admin:
    print("Please go to this office!")
elif is_guest or is_parent:
    # elif is_parent or is_guest:
    print("Waiting room is over there!")
else:
    print("Other cases")
