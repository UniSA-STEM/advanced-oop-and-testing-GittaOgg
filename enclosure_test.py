"""
File: enclosure_test.py
Description: test module for testing Enclosure module for advanced programming assignment
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import enclosure
import animal
import pytest

class TestEnclosure:
    '''
    Test class for the enclosure module
    '''

    @pytest.fixture
    def enclosure_1(self):
        return enclosure.Enclosure('Aviary 1','Small','Aviary')

    @pytest.fixture
    def enclosure_2(self):
        return enclosure.Enclosure('Reptile House 1','Medium','Desert')

    @pytest.fixture
    def enclosure_3(self):
        return enclosure.Enclosure('Jungle Zone 1','Large','Jungle')

    @pytest.fixture
    def reptile_1(self):
        return animal.Reptile('Bob',10,'perfect','Crocodile','meat')

    @pytest.fixture
    def mammal_1(self):
        return animal.Mammal('Jane',12,'perfect','Monkey','bananas')

    @pytest.fixture
    def reptile_2(self):
        return animal.Reptile('Dave',5,'perfect','Snake','meat')

    @pytest.fixture
    def reptile_3(self):
        return animal.Reptile('SickDave',5,'under treatment','Snake','meat')


    def test_enclosure(self, enclosure_1, enclosure_2, enclosure_3):
        # tests for correct setup of enclosures
        assert enclosure_1.name == 'Aviary 1'
        assert enclosure_2.size == 'Medium'
        assert enclosure_3.environment == 'Jungle'


    def test_add_animal(self, enclosure_3, reptile_1, reptile_2,reptile_3,mammal_1):
        # tests for adding animals to enclosures

        # adding reptile 1 to enclosure should raise key error. Crocodile has not had environment defined in dictionary
        with pytest.raises(KeyError):
            enclosure_3.add_animal(reptile_1)

        # mammal 1 should be able to be added to enclosure 3- meets all requirements
        enclosure_3.add_animal(mammal_1)
        assert enclosure_3.animals == [mammal_1]

        # reptile 2 should not be able to be added to enclosure when mammal 1 in there
        assert enclosure_3.add_animal(reptile_2) == 'Species is incompatible with current residents'

        # reptile 3 has health_status of under treatment and should be stopped from being moved into enclosure
        assert enclosure_3.add_animal(reptile_3) == 'SickDave is currently under treatment and cannot be moved'


    def test_remove_animal(self, enclosure_3, mammal_1):
        # simple add and remove animal test
        enclosure_3.add_animal(mammal_1)
        assert enclosure_3.remove_animal(mammal_1) == 'Jane has been removed from this enclosure'

