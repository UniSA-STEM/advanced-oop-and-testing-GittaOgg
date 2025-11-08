"""
File: enclosure.py
Description: ****DESCRIPTION*****
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""


class Enclosure():

    environments = {'Savannah','Aviary','Jungle','Aquatic','Desert','Arctic'}
    sizes = {'Small','Medium','Large','Extra Large'}

    def set_environment(self, environment):
        if environment not in Enclosure.environments:
            raise ValueError('Invalid environment')
        else:
            self.__environment = environment

    def set_size(self, size):
        if size not in Enclosure.sizes:
            raise ValueError('Invalid size')
        else:
            self.__size = size

    def __init__(self, name, size, environment):
        try:
            self.__name = name
            self.set_size(size)
            self.set_environment(environment)
            self.__cleanliness = 5
            self.__animals = []
        except ValueError as e:
            print(e)

    def __str__(self):
       return(f'{self.name} is a {self.size} enclosure of type: {self.environment}. Current cleanliness: '
             f'{self.cleanliness} Stars. ADD ANIMALS!!')

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


    name = property(get_name)
    size = property(get_size)
    environment = property(get_environment, set_environment)
    cleanliness = property(get_cleanliness, set_cleanliness)
    animals = property(get_animals)




e1 = Enclosure('lions1','Large','Savannah')
print(e1)
e2 = Enclosure('birds1','Small','Aviary')
print(e2)
e3 = Enclosure('lizards1','Mm','hothouse')

