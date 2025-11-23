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


@pytest.fixture
def reptile_1():
    return animal.Reptile('Bob',10,'perfect','Crocodile','meat')

@pytest.fixture
def reptile_2():
    return animal.Reptile('Sally',3,'under treatment','Snake','meat')

@pytest.fixture
def mammal_1():
    return animal.Mammal('Jane',12,'perfect','Monkey','bananas')

@pytest.fixture
def bird_1():
    return animal.bird('Geoff',2,'perfect','Cockatoo','bugs')

