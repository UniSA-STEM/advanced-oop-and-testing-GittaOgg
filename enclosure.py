"""
File: enclosure.py
Description: Enclosure module for advanced programming assignment containing enclosure class
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import animal

class Enclosure():
    '''
    A class which represents an enclosure

    Attributes
    ----------
    name: str
        Name of the enclosure
    size: str
        Size of the enclosure
    environment: str
        Environment of the enclosure
    cleanliness: int
        Cleanliness rating (1-5) of the enclosure
    animals: list
        List of animals within the enclosure


    Methods
    -------
    add_animal()
        returns message explaining if successful or unsuccessful in adding animal to enclosure
    remove_animal()
        returns message explaining if successful or unsuccessful in removing animal from enclosure

    '''

    Enclosure_list = []
    # set up of list of enclosures instantiated, for reporting purposes


    environments = {'Savannah','Aviary','Jungle','Aquatic','Desert','Arctic'}
    # set of allowable environments for any enclosure to have

    sizes = {'Small','Medium','Large','Extra Large'}
    # set of allowable sizes for any enclosure to be

    size_limits = {
        'Small': 5,
        'Medium': 10,
        'Large': 15,
        'Extra Large': 20
    }
    # dictionary of sizes and max allowable animals

    environment_animals = {
        'Lion': 'Savannah',
        'Giraffe': 'Savannah',
        'Cockatoo': 'Aviary',
        'Flamingo': 'Aviary',
        'Tiger': 'Jungle',
        'Monkey': 'Jungle',
        'Snake':'Jungle',
        'Lizard':'Desert',
        'Camel':'Desert',
        'Polar Bear':'Arctic',
        'Penguin':'Arctic'
    }
    # dictionary of animals and their environments

    def set_environment(self, environment):
        '''
        A method to set an enclosure's environment if the environment exists in the set 'environments'
        :param environment: str
        :return: ValueError or setting of environment
        '''
        if environment not in Enclosure.environments:
            raise ValueError('Invalid environment')
        else:
            self.__environment = environment

    def set_size(self, size):
        '''
        A method to set an enclosure's size if the size exists in the set 'sizes'
        :param size: str
        :return: ValueError or setting of size
        '''
        if size not in Enclosure.sizes:
            raise ValueError('Invalid size')
        else:
            self.__size = size

    def __init__(self, name:str, size:str, environment:str):
        try:
            self.__name = name
            self.set_size(size)
            self.set_environment(environment)
            self.__cleanliness = 5
            self.__animals = []
            Enclosure.Enclosure_list.append(self)
        except ValueError as e:
            print(e)

    def __str__(self):
       Animal_str = ''
       for animal in self.__animals:
           Animal_str += '* ' + animal + '\n'

       return(f'**** {self.name} ****\nSize: {self.size} \nType: {self.environment}\nCurrent cleanliness: '
             f'{self.cleanliness} Stars\nAnimals:\n{Animal_str}\n')

    def get_cleanliness(self):
        return self.__cleanliness

    def get_animals(self):
        return self.__animals

    def get_size(self):
        return self.__size

    def get_environment(self):
        return self.__environment

    def get_name(self):
        return self.__name

    def set_cleanliness(self, cleanliness):
        if 1<= cleanliness <= 5:
            self.__cleanliness = cleanliness
        else:
            print('cleanliness must be between 1 and 5 stars')

    def add_animal(self,animal):
        '''
        A method to add an animal to the enclosure if it complies with rules of environment, size, species mixing and
        animals under treatment
        :param animal: object of class Animal
        :return: KeyError or message explaining if successful or unsuccessful in adding animal to enclosure
        '''
        if animal.health_status == 'under treatment':
            # animals under treatment cannot be moved, check health status
            return(f'{animal.name} is currently under treatment and cannot be moved')
        else:
            if self.animals == [] or self.animals[0].species == animal.species:
                # Enclosures cannot hold more than 1 species, check if enclosure is empty or if existing animal
                # is the same species as the animal being added
                if len(self.animals) == self.size_limits[self.size]:
                    # size of enclosure dictates number of animals which can be held. Check enclosure capacity
                    return(f'This enclosure is {self.size} and has a maximum capacity of {self.size_limits[self.size]}'
                          f'\n{animal} cannot be added')
                else:
                    try:
                        # check the environment_animals dictionary to see what environment the species being added needs
                        # within try/catch in case of key error. species may not have been added to dictionary yet
                        if self.environment_animals[animal.species] != self.__environment:
                            return(f'{animal.species}s cannot be kept in this environment. Cannot be added')
                        else:
                            self.__animals.append(animal)
                            return(f'{animal.name} has been added to this enclosure')
                    except KeyError:
                        # if cannot find the animal in the environment_animals dictionary, raise KeyError and display messsage
                        raise KeyError('Cannot find environment for this animal')
            else:
                # if enclosure is currently holding animal of another species, return warning message
                return(f'Species is incompatible with current residents')


    def remove_animal(self,animal):
        '''
        A method to remove an animal from the enclosure if it exists within the enclosure
        :param animal: object of class Animal
        :return: Message advising of successful or unsuccessful removal of animal from enclosure
        '''
        if animal in self.animals:
            # check if animal is in this enclosure before removing
            self.animals.remove(animal)
            return(f'{animal.name} has been removed from this enclosure')
        else:
            # if animal is not here then return warning message
            return(f'{animal} not found in this enclosure')

    def enclosure_report(self):
        print('\n**** Enclosures at the Zoo ****')
        for enclosure in Enclosure.Enclosure_list:
            print(f'{enclosure.name} : {enclosure.size} {enclosure.environment} enclosure holding {len(enclosure.animals)} animals')

    def enclosure_capacity_report(self):
        print('\n**** Enclosures With Capacity ****')
        for enclosure in Enclosure.Enclosure_list:
            if len(self.animals) < self.size_limits[self.size]:
                print(f'{enclosure.name} : {enclosure.environment} with capacity for {self.size_limits[self.size] -len(enclosure.animals)} more animals')


    def enclosure_cleanliness_report(self):
        print('\n**** Enclosures Cleanliness ****')
        for enclosure in Enclosure.Enclosure_list:
            print(f'{enclosure.name} : {enclosure.cleanliness}')



    name = property(get_name)
    size = property(get_size)
    environment = property(get_environment, set_environment)
    cleanliness = property(get_cleanliness, set_cleanliness)
    animals = property(get_animals)





