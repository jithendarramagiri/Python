class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Taking input from user
name = input("Enter name: ")
age = int(input("Enter age: "))
person = Person(name, age)
person.display()