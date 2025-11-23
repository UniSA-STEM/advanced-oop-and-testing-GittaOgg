"""
File: staff_test.py
Description: test module for testing staff module for advanced programming assignment
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""

import staff
import animal
import enclosure
import pytest

class TestStaff:
    '''
    Test class for the staff module
    '''
    @pytest.fixture
    def zookeeper_1(self):
        return staff.Zookeeper('James Smith',5/5/2000,1/1/2020,60000)
    @pytest.fixture
    def zookeeper_2(self):
        return staff.Zookeeper('Max Power',1/1/1950,2/2/1975,80000)
    @pytest.fixture
    def vet_1(self):
        return staff.Vet('Ann Jones',8/8/1975,6/6/2000,100000)
    @pytest.fixture
    def vet_2(self):
        return staff.Vet('Miguel Sanchez',3/3/1980,1/1/2025,100000)
    @pytest.fixture
    def gift_shop_1(self):
        return staff.GiftShop('Mary Lady',4/4/2005,5/5/2025,25000)
    @pytest.fixture
    def mammal_1(self):
        return animal.Mammal('Jane',12,'perfect','Monkey','bananas')
    @pytest.fixture
    def mammal_2(self):
        return animal.Mammal('Jane2',12,'perfect','Monkey','bananas')
    @pytest.fixture
    def reptile_1(self):
        return animal.Reptile('Sally',3,'under treatment','Lizard','meat')
    @pytest.fixture
    def reptile_2(self):
        return animal.Reptile('Sally2', 3, 'under treatment', 'Lizard', 'meat')
    @pytest.fixture
    def reptile_3(self):
        return animal.Reptile('Sally3', 3, 'under treatment', 'Lizard', 'meat')
    @pytest.fixture
    def reptile_4(self):
        return animal.Reptile('Sally4', 3, 'under treatment', 'Lizard', 'meat')
    @pytest.fixture
    def enclosure_1(self):
        return enclosure.Enclosure('place1','Medium','Jungle')


    def test_zookeeper(self, zookeeper_1, zookeeper_2):
        # test that zookeepers are set up correctly
        assert zookeeper_1.name == 'James Smith'
        assert zookeeper_2.pay == 80000

    def test_zookeeper_schedule(self, zookeeper_1, zookeeper_2):
        # create schedule for 1 zookeeper
        zookeeper_1.create_schedule()
        # test that schedule is not empty for that zookeeper
        assert zookeeper_1.schedule != {}
        # test that schedule remains empty for zookeeper without schedule created
        assert zookeeper_2.schedule == {}

    def test_zookeeper_add_animal(self, zookeeper_1, mammal_1, mammal_2, reptile_1, reptile_2, reptile_3, reptile_4):
        # test adding animals to zookeeper's animals_to_feed list
        # add 5 animals to zookeeper_1's list (max allowable)
        zookeeper_1.add_animal(mammal_1)
        zookeeper_1.add_animal(mammal_2)
        zookeeper_1.add_animal(reptile_1)
        zookeeper_1.add_animal(reptile_2)
        zookeeper_1.add_animal(reptile_3)
        # test that there are 5 animals in their list
        assert len(zookeeper_1.animals_to_feed) == 5
        # test that cannot add a 6th animal to their list
        assert zookeeper_1.add_animal(reptile_4) == 'James Smith is assigned 5 animals and cannot be assigned any more. Please find another staff member to feed this animal'

    def test_zookeeper_add_enclosure(self, zookeeper_2, enclosure_1):
        # test adding enclosure to zookeeper's enclosures_to_clean list
        zookeeper_2.add_enclosure(enclosure_1)
        # check the length of their list has gone up to 1
        assert len(zookeeper_2.enclosures_to_clean) == 1

    def test_zookeeper_clean_enclosure(self,zookeeper_2, enclosure_1):
        # test cleaning of enclosures
        # manually set the cleanliness of enclosure to 1 star
        enclosure_1.cleanliness = 1
        # zookeeper cleans enclosure
        zookeeper_2.clean_enclosures(enclosure_1)
        # test that cleanliness of enclosure back to 5 stars after cleaning
        assert enclosure_1.cleanliness == 5

    def test_vet(self,vet_1, vet_2):
        # test set  up of vet
        assert vet_1.pay == 100000
        assert vet_2.name == 'Miguel Sanchez'

    def test_vet_create_schedule(self, vet_1, vet_2):
        # test creating schedules leads to non-blank schedule, when default for vet2 remains blank
        vet_1.create_schedule()
        assert vet_1.schedule != {}
        assert vet_2.schedule == {}

    def test_gift_shop(self, gift_shop_1):
        # test set up of gift shop staff
        assert gift_shop_1.name == 'Mary Lady'

    def test_gift_shop_opening(self,gift_shop_1):
        # test open shop method
        assert gift_shop_1.open_shop() == 'Mary Lady has opened the shop.'
