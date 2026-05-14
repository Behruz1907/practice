'''CLASS deep dive
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLIMORPHISM
    '''


print("==== INHERITANCE ====")
# PARENT > CHILD [only public & protected properties(state + method)]


class Animal(object):

    description = "The class is parent for animals"

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the {self.name} says: {self.sound}")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "Zzzz", False)


dog.introduce()
cat.introduce()
fish.introduce()


print("========")
dog.make_voice()
fish.make_voice()


print("========")
print(Animal.description)
print(dog.description)
print(fish.description)

print("========")
print(dog.voice, fish.voice)
print("dog.status:", dog._status)
# print("fish.status:", fish.status)
# print("cat.status:", cat.status)


# Bir narsaning bir necha xil shaklga ega bo'lishi yoki bir xil methodning turli xil shaklga ega bolishi
print("==== POLIMORPHISM ====")


dog.make_voice()
cat.make_voice()


print("========")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")


# Fish > Animal > object

data1 = issubclass(Fish, Animal)

data2 = issubclass(Animal, object)
print("data:", data1, data2)
