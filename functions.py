'''
FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''


print("====DEFINE vs CALL====")

# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


#  DEFINE - built
def greet(a):
    print(f"How do you do, {a}")


# CALL -execute
result1 = greet("RYAN")
print(f"result:", result1)

#  DEFINE - parametr


def alik(b):
    print(f"I'm pretty good and you?, {b}")


#  CALL - argument
alik("BEHRUZ")


def greeting(c):
    print("greeting is executed")
    return f"Hi {c}"


result2 = greeting("Justin")
print("result2:", result2)


print("==== Keyword & default arguments ====")

#  DEFINE


def give_greet(name, age=22):
    print("give_geet is executed")
    return f"Hi {name}, you are {age} years old!"


#  CALL
# BUNING ASOSIY MAQSADI bizning soursimizni ishlatadigan odamni tushunishi oson bolishi uchun! bu == comments
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)


result4 = give_greet("John")
print("result4:", result4)

print("==== Scope ====")

b = 100  # 3


# DEFINE
def calculate(a):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5)

g = 100


def findLetter(j):
    k = j + g
    print(f"just test: {k}")


findLetter(9)
