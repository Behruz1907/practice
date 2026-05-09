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

print("====Parametr vs Argument====")
