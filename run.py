
# Dunder __builtins__, ---> pythonning system variable   __init__ ---> bu pythondi magic methodi va negizi


message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)


'''
In Python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTION > print() len() input() type()
(3) CONSTANTS > True False None

'''

print(dir(__builtins__))
