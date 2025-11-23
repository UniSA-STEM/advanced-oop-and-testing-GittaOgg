"""
File: animal_test.py
Description: test module for testing Animal module for advanced programming assignment
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import animal
import pytest

class TestAnimals:
    '''
    Test class for the animal module
    '''

    @pytest.fixture
    def reptile_1(self):
        return animal.Reptile('Bob',10,'perfect','Crocodile','meat')

    @pytest.fixture
    def reptile_2(self):
        return animal.Reptile('Sally',3,'under treatment','Lizard','meat')

    @pytest.fixture
    def mammal_1(self):
        return animal.Mammal('Jane',12,'perfect','Monkey','bananas')

    @pytest.fixture
    def bird_1(self):
        return animal.Bird('Geoff',2,'perfect','Cockatoo','bugs')

    def test_mammal(self,mammal_1):
        # Tests mammals are setup correctly
        assert mammal_1.name == 'Jane'

    def test_mammal_cry(self,mammal_1):
        # tests the Mammal's cry method
        assert mammal_1.cry() == 'Jane says OOK OOK'

    def test_reptile(self,reptile_1,reptile_2):
        # tests reptiles set up correctly
        assert reptile_1.name == 'Bob'
        assert reptile_2.age == 3
        assert reptile_1.species == 'Crocodile'
        assert reptile_2.dietary_requirements == 'meat'

    def test_reptile_sleep(self,reptile_1,reptile_2):
        # Tests the Reptile's sleep method
        assert reptile_1.sleep() == 'Bob sleeps like a reptile'
        assert reptile_2.sleep() == 'Sally sleeps like a reptile'

    def test_reptile_cry(self,reptile_1,reptile_2):
        # tests the Reptile's cry method
        assert reptile_1.cry() == 'Bob says SNAP SNAP'
        assert reptile_2.cry() == 'Sally says MYSTERY NOISE'

    def test_bird(self,bird_1):
        # Tests birds are setup correctly
        assert bird_1.age == 2
        assert bird_1.species == 'Cockatoo'

    def test_bird_cry(self,bird_1):
        # tests the bird's cry method
        assert bird_1.cry() == 'Geoff says tweet tweet!!'

    def test_bird_flies(self,bird_1):
        # tests the bird's fly method
        assert bird_1.fly() == 'Geoff flies like a bird'