"""
File: animal.py
Description: ****DESCRIPTION*****
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age, health_status, species, dietary_requirements):
        self.name = name
        self.age = age
        self.health_status = health_status
        self.species = species
        self.dietary_requirements = dietary_requirements


    def __str__(self):
        return(f'{self.name} is {self.age} years old. They are a {self.species} with {self.dietary_requirements} dietary '
              f'requirements. {self.name}\'s current health is {self.health_status}.')

    def __eq__(self, other):
        self.name = other.name
        self.age = other.age
        self.species = other.species

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Bird(Animal):

    def __init__(self, name, age, health_status, species, dietary_requirements):
        super().__init__(name,age, health_status,species,dietary_requirements)


    def __str__(self):
        return f'BIRD: ' + super().__str__()


    def cry(self):
        print(f'{self.name} says tweet tweet!!')

    def eat(self):
        print(f'{self.name} eats like a bird')

    def sleep(self):
        print(f'{self.name} sleeps like a bird')

    def fly(self):
        print(f'{self.name} flies like a bird')

    def lay_egg(self):
        print(f'{self.name} has laid an egg')


class Mammal(Animal):

    def __init__(self, name, age, health_status, species, dietary_requirements):
        super().__init__(name, age, health_status, species, dietary_requirements)

    def __str__(self):
        return f'MAMMAL: ' + super().__str__()

    def cry(self):
        if self.species == 'lion':
            print(f'{self.name} says ROAR')
        elif self.species == 'monkey':
            print(f'{self.name} says OOK OOK')
        elif self.species == 'elephant':
            print(f'{self.name} says TRUMPET')
        else:
            print(f'{self.name} says ANOTHER NOISE')


    def eat(self):
        print(f'{self.name} eats like a mammal')

    def sleep(self):
        print(f'{self.name} sleeps like a mammal')

    def give_birth(self):
        print(f'{self.name} has given birth')


class Reptile(Animal):

    def __init__(self, name, age, health_status, species, dietary_requirements):
        super().__init__(name, age,health_status,species,dietary_requirements)

    def __str__(self):
        return f'REPTILE: ' + super().__str__()

    def cry(self):
        if self.species == 'snake':
            print(f'{self.name} says HISSSSS')
        elif self.species == 'crocodile':
            print(f'{self.name} says SNAP SNAP')
        else:
            print(f'{self.name} says ANOTHER NOISE')

    def eat(self):
        print(f'{self.name} eats like a reptile')

    def sleep(self):
        print(f'{self.name} sleeps like a reptile')

    def lay_egg(self):
        print(f'{self.name} has laid an egg')



m1 = Mammal('bob',10,'perfect','lion','meat')
m2 = Mammal('didi',10,'ok','elephant','leaves')
m3 = Mammal('penny',5,'good','meerkat','bugs')

print(m1)
print(m2)
print(m3)

m1.cry()
m2.cry()
m3.cry()
m2.eat()
m3.sleep()