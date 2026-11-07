# Method Overiding

class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark bark"
class Cat(Animal):
    def sound(self):
        return "Meow meow"
# Taking input from user
animal_type = input("Enter animal type (Dog/Cat): ")
if animal_type == "Dog":
    animal = Dog()
elif animal_type == "Cat":
    animal = Cat()
else:
    print("Invalid animal type")
    animal = None
if animal:
    print(f"Sound: {animal.sound()}")
