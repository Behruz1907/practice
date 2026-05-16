'''Tuple
 (1) What is tuple: typle vs list
 (2) Unpacking arguments
 (3) zip
 '''

print("==== What is tuple: typle vs list ==== ")
#  Java/PHP/NodeJS array > Python list, array > special holatlarda ishlatamiz pyton dagi arrayni

#  literal
numbs = [3, 5, 1, 2]
print(numbs)

#  constructor function
letters = list("Hello World!")
print(letters)


fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)


#  tuple --- biz tuplening ichida foydalanilgan qiymatlarni o'zgartirolmemiz

animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "tiger"


# try avoid this imkon qadar kam ishlat bunday holatlarni
people = "Andrew", "John"
animals = "dog",


print("==== Unpacking arguments ==== ")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("======")
calculate(0, 2, 300)
print("======")
calculate(5, 7)


# **kwargs > dictionary
def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi I am {kwargs["name"]} and I am {kwargs["age"]} years old!")
    pass


# CALL
introduce(name="Justin", age=28)
introduce(name="Shawn", age=30, single=True)


def greeting(*args, **kwargs):
    print("args >", args)
    print("**kwargs", kwargs)


# CALL
greeting("hi", True, 19, name="Ryan", age=20)


print("==== zip ==== ")

tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c")


zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
result = list(zipped)
print(result)
