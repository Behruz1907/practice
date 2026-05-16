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
