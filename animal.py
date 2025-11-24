"""
File: animal.py
Description: animal module for advanced programming assignment containing Animal class and children
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    '''
    An abstract class which represents an animal for Bird, Mammal and Reptile to inherit from

    Attributes
    ----------
    name : str
        Animal's name
    age: int
        Animal's age
    health_status: str
        Animal's health status, either 'perfect' or 'under treatment'
    health_issues: list
        list of any health issues associated with animal
    species: str
        Animal's species
    dietary_requirements: str
        Animal's dietary requirements


    Methods
    -------
    cry:
        abstract class for inheritance

    eat:
        abstract class for inheritance

    sleep:
        abstract class for inheritance

    '''
    Animal_list = []
    # set up of empty list of animals at zoo

    def __init__(self, name:str, age:int, health_status:str, species:str, dietary_requirements:str):
        self.name = name
        self.age = age
        self.health_status = health_status
        self.health_issues = []
        self.species = species
        self.dietary_requirements = dietary_requirements
        Animal.Animal_list.append(self)
        # when animal is instantiated, added to Animal_list for reporting purposes


    def __str__(self):
        return(f'{self.name}- {self.age} year old {self.species}\nDiet: {self.dietary_requirements}'
              f'\nCurrent health: {self.health_status}\n****************************')

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
    '''
    A class which represents a Bird,inherited from abstract class Animal

    Attributes
    ----------
    name : str
        Animal's name
    age: int
        Animal's age
    health_status: str
        Animal's health status, either 'perfect' or 'under treatment'
    health_issues: list
        list of any health issues associated with animal
    species: str
        Animal's species
    dietary_requirements: str
        Animal's dietary requirements


    Methods
    -------
    cry():
        returns message of bird's cry
    eat():
        returns message of bird eating diet
    sleep():
        returns message of bird sleeping
    fly():
        returns message of bird flying
    '''


    def __init__(self, name:str, age:int, health_status:str, species:str, dietary_requirements:str):
        super().__init__(name,age, health_status,species,dietary_requirements)


    def __str__(self):
        return f'\nBIRD:\n' + super().__str__()


    def cry(self):
        '''
        A method for the bird to cry
        :return: message of bird's cry
        '''
        return(f'{self.name} says tweet tweet!!')

    def eat(self):
        '''
        A method for the bird to eat
        :return: message of bird's eating
        '''
        return(f'{self.name} eats {self.dietary_requirements} like a bird')

    def sleep(self):
        '''
        A method for the bird to sleep
        :return: message of bird's sleeping
        '''
        return(f'{self.name} sleeps like a bird')

    def fly(self):
        '''
        A method for the bird to fly
        :return: message of bird's flying
        '''
        return(f'{self.name} flies like a bird')

    def bird_treatment_report(self):
        print('\n**** Birds under Treatment ****')
        for bird in Animal.Animal_list:
            if bird.__class__.__name__ == 'Bird':
                if bird.health_status == 'under treatment':
                    print(f'{bird.name}')

    def bird_report(self):
        print('\n**** Birds at the Zoo ****')
        for bird in Animal.Animal_list:
            if bird.__class__.__name__ == 'Bird':
                print(f'{bird.name} : {bird.age} yr old {bird.species}')



class Mammal(Animal):
    '''
    A class which represents a Mammal,inherited from abstract class Animal

    Attributes
    ----------
    name : str
        Animal's name
    age: int
        Animal's age
    health_status: str
        Animal's health status, either 'perfect' or 'under treatment'
    health_issues: list
        list of any health issues associated with animal
    species: str
        Animal's species
    dietary_requirements: str
        Animal's dietary requirements


    Methods
    -------
    cry():
        returns message of mammal's cry
    eat():
        returns message of mammal eating diet
    sleep():
        returns message of mammal sleeping

    '''
    def __init__(self, name:str, age:int, health_status:str, species:str, dietary_requirements:str):
        super().__init__(name, age, health_status, species, dietary_requirements)

    def __str__(self):
        return f'\nMAMMAL:\n' + super().__str__()

    def cry(self):
        '''
        A method for the mammal to cry
        :return: message of mammal's cry
        '''
        match self.species:
            case 'Lion':
                return(f'{self.name} says ROAR')
            case 'Monkey':
                return(f'{self.name} says OOK OOK')
            case 'Elephant':
                return(f'{self.name} says TRUMPET')
            case default:
                return(f'{self.name} says MYSTERY NOISE')


    def eat(self):
        '''
        A method for the mammal to eat
        :return: message of mammal's eating
        '''
        return(f'{self.name} eats {self.dietary_requirements} like a mammal')

    def sleep(self):
        '''
        A method for the mammal to sleep
        :return: message of mammal's sleeping
        '''
        return(f'{self.name} sleeps like a mammal')

    def mammal_treatment_report(self):
        print('\n**** Mammals under Treatment ****')
        for mammal in Animal.Animal_list:
            if mammal.__class__.__name__ == 'Mammal':
                if mammal.health_status == 'under treatment':
                    print(f'{mammal.name}')

    def mammal_report(self):
        print('\n**** Mammals at the Zoo ****')
        for mammal in Animal.Animal_list:
            if mammal.__class__.__name__ == 'Bird':
                print(f'{mammal.name} : {mammal.age} yr old {mammal.species}')



class Reptile(Animal):
    '''
        A class which represents a Reptile,inherited from abstract class Animal

        Attributes
        ----------
        name : str
            Animal's name
        age: int
            Animal's age
        health_status: str
            Animal's health status, either 'perfect' or 'under treatment'
        health_issues: list
            list of any health issues associated with animal
        species: str
            Animal's species
        dietary_requirements: str
            Animal's dietary requirements


        Methods
        -------
        cry():
            returns message of reptile's cry
        eat():
            returns message of reptile eating diet
        sleep():
            returns message of reptile sleeping

    '''
    def __init__(self, name:str, age:int, health_status:str, species:str, dietary_requirements:str):
        super().__init__(name, age,health_status,species,dietary_requirements)

    def __str__(self):
        return f'\nREPTILE:\n' + super().__str__()

    def cry(self):
        '''
        A method for the reptile to cry
        :return: message of reptile's cry
        '''
        match self.species:
            case 'Snake':
                return(f'{self.name} says HISSSS')
            case 'Crocodile':
                return(f'{self.name} says SNAP SNAP')
            case default:
                return(f'{self.name} says MYSTERY NOISE')


    def eat(self):
        '''
        A method for the reptile to eat
        :return: message of reptile's eating
        '''
        return(f'{self.name} eats {self.dietary_requirements} like a reptile')

    def sleep(self):
        '''
        A method for the reptile to sleep
        :return: message of reptile's sleeping
        '''
        return(f'{self.name} sleeps like a reptile')

    def reptile_treatment_report(self):
        print('\n**** Reptiles under Treatment ****')
        for reptile in Animal.Animal_list:
            if reptile.__class__.__name__ == 'Reptile':
                if reptile.health_status == 'under treatment':
                    print(f'{reptile.name}')

    def reptile_report(self):
        print('\n**** Reptiles at the Zoo ****')
        for reptile in Animal.Animal_list:
            if reptile.__class__.__name__ == 'Reptile':
                print(f'{reptile.name} : {reptile.age} yr old {reptile.species}')



