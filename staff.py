"""
File: staff.py
Description: ****DESCRIPTION*****
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod

class Staff(ABC):

    def __init__(self, name, dob, start_date, pay):
        self.name = name
        self.dob = dob
        self.start_date = start_date
        self.pay = pay


    def __str__(self):
        return f'** {self.name} DOB: {self.dob} **\nStart Date: {self.start_date}\nPay: {self.pay}'

    def __eq__(self, other):
        return self.name == other.name and self.dob == other.dob and self.start_date == other.start_date

    @abstractmethod
    def create_schedule(self):
        pass


    @abstractmethod
    def check_schedule(self):
        pass

class Zookeeper(Staff):
    def __init__(self, name, dob, start_date, pay):
        super().__init__(name,dob,start_date,pay)
        self.enclosures_to_clean = []
        self.animals_to_feed = []

    def __str__(self):
        return '**** ZOOKEEPER ****' + super().__str__()

    def create_schedule(self):
        pass

    def check_schedule(self):
        pass

    def add_enclosure(self, enclosure):
        pass

    def add_animal(self, animal):
        pass

    def clean_enclosure(self, enclosure):
        pass

    def feed_animals(self):
        pass


class Vet(Staff):
    def __init__(self, name, dob, start_date, pay):
        super().__init__(name,dob,start_date,pay)
        self.animals_under_care = []

    def __str__(self):
        return '**** VET ****' + super().__str__()

    def create_schedule(self):
        pass

    def check_schedule(self):
        pass

    def perform_health_check(self):
        pass

    def perform_surgery(self):
        pass

    def mark_health_issue_resolved(self):
        pass

    def pronounce_death(self):
        pass


class GiftShop(Staff):
    def __init__(self, name, dob, start_date, pay):
        super().__init__(name,dob,start_date,pay)
        self.schedule = {}

    def __str__(self):
        return '**** GIFT SHOP WORKER ****' + super().__str__()

    def create_schedule(self):
        schedule = {
            '9:00am': 'Open Shop',
            '9:30am': 'Serve Customers',
            '10:00am': 'Serve Customers',
            '10:30am': 'Serve Customers',
            '11:00am':'Stock Shelves',
            '11:30am': 'Serve Customers',
            '12:00pm': 'Clean Shop',
            '12:30pm': 'Serve Customers',
            '1:00pm': 'Serve Customers',
            '1:30pm': 'Serve Customers',
            '2:00pm': 'Stock Shelves',
            '2:30pm': 'Serve Customers',
            '3:00pm': 'Serve Customers',
            '3:30pm': 'Serve Customers',
            '4:00pm': 'Close Shop',
        }
        self.schedule = schedule


    def check_schedule(self):
        for key, value in self.schedule.items():
            print(f'{key}: {value}')

    def open_shop(self):
        return f'{self.name} has opened the shop.'

    def stock_shelves(self):
        return f'{self.name} has stocked the shelves'

    def clean_shop(self):
        return f'{self.name} has cleaned the shop.'

    def serve_customers(self):
        return f'{self.name} has served the customers.'

    def close_shop(self):
        return f'{self.name} has closed the shop.'

