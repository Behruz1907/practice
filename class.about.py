'''CLASS
     (1) What is class
     (2) ordinary vs static properties
     (3) special methods
'''

print("==== What is class ====")
# class - blueprint for object creation!
# srtucture > state, constructor, method


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"the {self.name} says: How do you do!")

    def say_age(self):
        print(f"the {self.name} says: I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state

print("person1.name:", person1.name)

# ordinary state = oddiy state va oddiy methodlar
# static method = class bn yashedigan methodlar objectga daxli yoq! class bn birga keladigan propertylar
person1.introduce()
person2.say_age()


print("==== ordinary vs static properties ====")
# static state
new_message = Person.message
print("new_message", new_message)

# static method
Person.explain()
