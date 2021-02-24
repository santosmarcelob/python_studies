# Python OOP exercise - Cats Everywhere

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 adding another cat
class Willy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Creating a list of all the pets
my_cats = [Simon('Simon', 4), Sally('Sally', 3), Willy('Willy', 8)]

#3 Instantiating the Pet class
my_pets = Pets(my_cats)

#4 Output all of the cats walking
my_pets.walk()