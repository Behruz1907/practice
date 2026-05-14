'''CLASS deep dive
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLIMORPHISM
    '''


print("==== INHERITANCE ====")
# PARENT > CHILD [only public & protected properties(state + method)]


class Animal:

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
