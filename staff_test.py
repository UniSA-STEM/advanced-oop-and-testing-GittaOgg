"""
File: staff_test.py
Description: test module for testing staff module for advanced programming assignment
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""

import staff
import pytest

@pytest.fixture
def zookeeper_1():
    return staff.Zookeeper('James Smith',5/5/2000,1/1/2020,60000)

@pytest.fixture
def zookeeper_2():
    return staff.Zookeeper('Max Power',1/1/1950,2/2/1975,80000)

@pytest.fixture
def vet_1():
    return staff.Vet('Ann Jones',8/8/1975,6/6/2000,100000)

@pytest.fixture
def vet_2():
    return staff.Vet('Miguel Sanchez',3/3/1980,1/1/2025,100000)

@pytest.fixture
def gift_shop_1():
    return staff.GiftShop('Mary Lady',4/4/2005,5/5/2025,25000)
