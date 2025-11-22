"""
File: staff.py
Description: ****DESCRIPTION*****
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
import random

class Staff(ABC):

    Staff_list = []

    def __init__(self, name, dob, start_date, pay):
        self.name = name
        self.dob = dob
        self.start_date = start_date
        self.pay = pay
        Staff.Staff_list.append(self)


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
        self.max_enclosures = 5
        self.max_animals = 10

    def __str__(self):
        return '**** ZOOKEEPER ****' + super().__str__()

    def create_schedule(self):
        time_list = ['6:00am','7:00am','8:00am','9:00am','10:00am','11:00am','12:00pm','1:00pm','2:00pm']

        cleaning_list = []
        for enclosure in self.enclosures_to_clean:
            cleaning_list.append(f'Clean {enclosure.name} enclosure')

        feeding_list = []
        for animal in self.animals_to_feed:
            feeding_list.append(f'Feed {animal.dietary_requirements} to {animal.name} the {animal.species}')

        work_list = cleaning_list + feeding_list

        while len(work_list) < 9:
            work_list.append('Ad hoc duties')

        self.schedule = dict(zip(time_list, work_list))

        for key, value in self.schedule.items():
            print(f'{key}: {value}')



    def add_enclosure(self, enclosure):
        if len(self.enclosures_to_clean) < self.max_enclosures:
            self.enclosures_to_clean.append(enclosure)
        else:
            print(f'{self.name} is assigned {self.max_enclosures} enclosures and cannot be assigned any more. Please '
                  f'find another staff member to clean this enclosure')

    def add_animal(self, animal):
        if len(self.animals_to_feed) < self.max_animals:
            self.animals_to_feed.append(animal)
        else:
            print(f'{self.name} is assigned {self.max_animals} animals and cannot be assigned any more. Please find '
                  f'another staff member to feed this animal')

    def clean_enclosures(self):
        for enclosure in self.enclosures_to_clean:
            enclosure.set_cleanliness(5)
            print(f'{enclosure.name} has been cleaned to {enclosure.cleanlines} star rating')


    def feed_animals(self):
        for animal in self.animals_to_feed:
            print(f'{animal.name} has been fed {animal.dietary_requirements}')


class Vet(Staff):
    def __init__(self, name, dob, start_date, pay):
        super().__init__(name,dob,start_date,pay)
        self.animals_under_care = []
        self.max_animals = 50

    def __str__(self):
        return '**** VET ****' + super().__str__()

    def create_schedule(self):
        time_list = ['9:00am','10:00am','11:00am','12:00pm','1:00pm','2:00pm','3:00pm','4:00pm','5:00pm']
        surgery_list = []
        therapy_list = []
        first_aid_list = []
        health_check_list = []
        for animal in self.animals_under_care:
            health_check_list.append(f'{animal.name} health check')
            for issue in animal.health_issues:
                if issue.treatment_plan=='surgery':
                    surgery_list.append(f'{animal.name} surgery for {issue}')
                elif issue.treatment_plan=='therapy':
                    therapy_list.append(f'{animal.name} therapy for {issue}')
                elif issue.treatment_plan=='first_aid':
                    first_aid_list.append(f'{animal.name} first aid for {issue}')
        work_list = surgery_list + therapy_list + first_aid_list + health_check_list

        while len(work_list) < 9:
            work_list.append('Ad hoc duties')

        while len(work_list) > 9:
            overflow = []
            overflow.append(work_list[9])
            work_list.pop(9)
            overflow_str = ''
            for item in overflow:
                overflow_str += f'{item}\n'

        self.schedule = dict(zip(time_list, work_list))

        for key, value in self.schedule.items():
            print(f'{key}: {value}')

        print(f'Extra Work List: \n{overflow_str}')


    def add_animal(self, animal):
        if len(self.animals_under_care) < self.max_animals:
            self.animals_under_care.append(animal)
        else:
            print(f'{self.name} is assigned {self.max_animals} animals and cannot be assigned any more. Please find '
                  f'another staff member to provide care for this animal')


    def perform_health_check(self, animal):
        sick = random.randint(1,10)
        if animal.health_status =='perfect' and sick == 10:
            animal.health_status = 'under treatment'
            print(f'{animal.name} has been declared under treatment')
        elif animal.health_status == 'under treatment' and sick > 5:
            animal.health_status = 'perfect'
            print(f'{animal.name} has been declared healed')
        else:
            print(f'{animal.name} is still {animal.health_status}')

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
        self.schedule = {
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

