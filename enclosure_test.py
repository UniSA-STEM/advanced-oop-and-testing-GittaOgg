"""
File: enclosure_test.py
Description: test module for testing Enclosure module for advanced programming assignment
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""
import enclosure
import pytest


@pytest.fixture
def enclosure_1():
    return enclosure.Enclosure('Aviary 1','Small','Aviary')

@pytest.fixture
def enclosure_2():
    return enclosure.Enclosure('Reptile House 1','Medium','Desert')

@pytest.fixture
def enclosure_3():
    return enclosure.Enclosure('Jungle Zone 1','Large','Jungle')

