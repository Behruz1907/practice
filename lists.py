'''LIST
(1) Working with lists
(2) List methods
(3) Lambda function
(4) enumerate, map and filter
'''


print("===== Working with lists =====")
#  Java/PHP/NodeJS array > Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]

for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World1")
print(f"the letters: {letters} and size: {len(letters)}")


print("======")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("===== List methods =====")

# methods > append() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind ohiridan qoshadi
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front oldidan qoshad
print(f"the insert result: {letters}")


size = len(letters) - 1
result = letters.pop(size)  # pop behind dan uzib beradi
print(f"the pop result: {result} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")


print("========")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("remove:", animals)


del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)


animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("value"))
else:
    print("cat does not exist")


print("========")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable > sorted function & index
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_nums: {new_numbs}")


print("===== Lambda function =====")
# lambda is a small anonymous funtion
def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)


people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()
print("people(1):", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)

print("===== enumerate, map and filter =====")
# enumerate for index and value

animals = ["dog", "cat"]
for element in enumerate(animals):
    print("element:", element)


for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")


# similar in disctionaries
car_obj = dict(brand="Ferrari", year=2025)
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {index} and value: {value}")

print("===== Map =====")

cars = [
    ("nexia", 78),
    ("cobalt", 88),
    ("zaparoj", 116),
    ("07 juguli", 109),
    ("malibu", 33)

]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_cars:", new_cars)


result_map = map(lambda car: car[0], cars)
print(f"the result_map: {result_map} and type {type(result_map)}")
new_cars = list(result_map)
print("new_cars(2)", new_cars)


print("===== filter =====")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type {type(result_filter)}")
print(list(result_filter))
