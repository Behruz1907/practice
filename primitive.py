print("==== numbers ====")

#  in JAVA, variable is a name storage location!
# in Python, variable is named reference!

count = 100
count_type = type(count)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("==== string ====")

#  METHODS: upper() lower() title() find() replace()

course = "MERN Python Fullstack"
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")


result = course.upper()
print(f"the result (3): {result}")


result = course.replace("Fullstack", "Masterclass")
print(f"the result (3): {result}")

print(course)


print("==== boolean ====")
#  functions > type() input() bool() int() str()
y = input("Give your value for y")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

#  TRUTHY vs FALSE value
# TRUTHY > True
#  FALSY > False

test_falsy = "" or False or None or 0
print("The FALSY:", bool(test_falsy))


test_falsy = "BEHRUZ"
print("The TRUTHY:", bool(test_falsy))
