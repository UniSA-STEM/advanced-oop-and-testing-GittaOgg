"""
File: staff.py
Description: Staff module for advanced programming assignment containing staff abstract class and children
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
import random
import health_issues
import animal
import enclosure


class Staff(ABC):
    '''
    An abstract class which represents a staff member for Zookeeper, Vet and GiftShop to inherit from

    Attributes
    ----------
    name : str
        Staff member's full name
    dob : date
        Staff member's Date of birth
    start_date : date
        Staff member's start date with zoo
    pay : float
        Staff member's annual pay

    Methods
    -------
    create_schedule()
        abstract method for creating a schedule

    '''
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


class Zookeeper(Staff):
    '''
    A class which represents a zookeeper. Inherits from abstract class Staff.

    Attributes
    ----------
    name : str
        Zookeeper's full name
    dob : date
        Zookeeper's Date of birth
    start_date : date
        Zookeeper's start date with zoo
    pay : float
        Zookeeper's annual pay
    enclosures_to_clean: list
        List of enclosures Zookeeper cleans
    animals_to_feed: list
        List of animals Zookeeper feeds
    max_enclosures : int
        Maximum number of enclosures Zookeeper can have assigned to them
    max_animals: int
        Maximum number of animals Zookeeper can have assigned to them
    schedule : dict
        Zookeeper's daily schedule

    Methods
    -------

    create_schedule()
    Returns schedule of times and tasks to be done

    add_enclosure()
    Returns message that enclosure was added to Zookeeper's care, or that Zookeeper is at capacity and enclosure cannot be added

    add_animal(animal)
    Returns message that animal was added to Zookeeper's care, or that Zookeeper is at capacity and animal cannot be added

    clean_enclosure()
    Returns message that enclosure was cleaned to 5-star cleanliness

    feed_animals()
    Returns message that animal was fed their diet

    '''

    def __init__(self, name, dob, start_date, pay):
        super().__init__(name,dob,start_date,pay)
        self.enclosures_to_clean = []
        self.animals_to_feed = []
        self.max_enclosures = 4
        self.max_animals = 5
        self.schedule = {}

    def __str__(self):
        return '**** ZOOKEEPER ****' + super().__str__()

    def create_schedule(self):
        '''
        Creates and displays a schedule for the Zookeeper including cleaning enclosures and feeding animals under their care.
        Zookeepers work 6am to 2pm and each task takes 1 hour
        :return: prints a schedule for the Zookeeper with times and tasks
        '''

        time_list = ['6:00am','7:00am','8:00am','9:00am','10:00am','11:00am','12:00pm','1:00pm','2:00pm']
        # set up time list with hourly intervals

        cleaning_list = []
        # set up empty cleaning list ready for enclosures to be added
        for enclosure in self.enclosures_to_clean:
            cleaning_list.append(f'Clean {enclosure.name} enclosure')
        # add all enclosures under care to cleaning list

        feeding_list = []
        # set up of empty feeding list ready for animals to be added
        for animal in self.animals_to_feed:
            feeding_list.append(f'Feed {animal.dietary_requirements} to {animal.name} the {animal.species}')
        # add all animals under care to feeding list

        work_list = cleaning_list + feeding_list
        # combine cleaning and feeding lists into work list

        # zookeepers have 9 intervals to work, the work list may have less work than required depending on the number
        # of animals and enclosures under their care.
        # max limits on animals and enclosures ensure there is never more than 9 things to do in 1 day
        while len(work_list) < 9:
            #if work list has less than 9 items, continue to add 'ad hoc duties' to the list until 9 items are present
            work_list.append('Ad hoc duties')

        # with 9 time intervals and 9 tasks, create dictionary of times and associated tasks and set as Zookeeper's schedule
        self.schedule = dict(zip(time_list, work_list))

        # print header for schedule
        print(f'**** {self.name}\'s schedule ****\n')
        # print the details of the schedule (key and value pairs from dictionary)
        for key, value in self.schedule.items():
            print(f'{key}: {value}')

    def add_enclosure(self, enclosure):
        '''
        Method to add enclosure to Zookeeper's enclosures_to_clean list.
        Checks that zookeeper has capacity to take on another enclosure

        :param enclosure: object of class Enclosure
        :return: if Zookeeper has capacity: message that enclosure was added to their care
        if Zookeeper has reached capacity: message that enclosure could not be added
        '''
        if len(self.enclosures_to_clean) < self.max_enclosures:
            # check if length of enclosures_to_clean list is less than max allowed
            self.enclosures_to_clean.append(enclosure)
            # add new enclosure to zookeeper's list
            print(f'{enclosure.name} has been added to {self.name}\'s care list')
            # advise user enclosure added
        else:
            print(f'{self.name} is assigned {self.max_enclosures} enclosures and cannot be assigned any more. Please '
                  f'find another staff member to clean this enclosure')
            # advise user zookeeper cannot take on any more enclosures

    def add_animal(self, animal):
        '''
        Method to add an animal to the Zookeeper's animals_to_feed list.
        Checks that zookeeper has capacity to take on another animal

        :param animal: object of class Animal
        :return: if Zookeeper has capacity: message that animal was added to their care
        if Zookeeper has reached capacity: message that animal could not be added
        '''
        if len(self.animals_to_feed) < self.max_animals:
            # check if length of amimals_to_feed list is less than max allowed
            self.animals_to_feed.append(animal)
            # add animal to zookeeper's list
            return(f'{animal.name} has been added to {self.name}\'s care list')
            # advise user animal was added
        else:
            return(f'{self.name} is assigned {self.max_animals} animals and cannot be assigned any more. Please find '
                  f'another staff member to feed this animal')
            # advise user zookeeper cannot take any more animals

    def clean_enclosures(self, enclosure):
        '''
        Method to clean enclosure
        :param enclosure: object of class Enclosure
        :return: message advising user enclosure was cleaned
        '''
        enclosure.set_cleanliness(5)
        # reset enclosure's cleanliness rating to 5
        return(f'{enclosure.name} has been cleaned to {enclosure.cleanliness} star rating')
        # advise user of cleaning

    def feed_animals(self, animal):
        '''
        Method to feed animal
        :param animal: object of class Animal
        :return: message advising user animal was fed
        '''
        return(f'{animal.name} has been fed {animal.dietary_requirements}')
        # advise user that animal was fed their diet

    def zookeeper_report(self):
        print('\n**** Zookeepers at the Zoo ****')
        for staff in Staff.Staff_list:
            if staff.__class__.__name__ == 'Zookeeper':
                print(staff.name)

    def zookeeper_can_clean_report(self):
        print('\n**** Zookeepers with Capacity for Additional Enclosures ****')
        for staff in Staff.Staff_list:
            if staff.__class__.__name__ == 'Zookeeper':
                if len(staff.enclosures_to_clean) < self.max_enclosures:
                    print(f'{staff.name} : capacity = {self.max_enclosures - len(staff.enclosures_to_clean)} enclosures')

    def zookeeper_can_feed_report(self):
        print('\n**** Zookeepers with Capacity for Additional Animals ****')
        for staff in Staff.Staff_list:
            if staff.__class__.__name__ == 'Zookeeper':
                if len(staff.animals_to_feed) < self.max_animals:
                    print(f'{staff.name} : capacity = {self.max_animals - len(staff.animals_to_feed)} animals')

class Vet(Staff):
    '''
    A class which represents a vet. Inherits from abstract class Staff.

    Attributes
    ----------
    name : str
        Vet's full name
    dob : date
        Vet's Date of birth
    start_date : date
        Vet's start date with zoo
    pay : float
        Vet's annual pay
    animals_under_care: list
        List of objects of class: Animal which are placed under vet's care
    max_animals : int
        The maximum number of animals a vet can have under their care
    schedule : dict
        Vet's daily schedule

    Methods
    -------

    create_schedule()
    Returns schedule of times and tasks to be done

    add_animal(animal)
    Returns message that animal was added to vet's care, or that vet is at capacity and animal cannot be added

    perform_health_check(animal)
    Returns message advising outcome of health check: animal is either perfect or under treatment

    '''
    def __init__(self, name, dob, start_date, pay):
        super().__init__(name,dob,start_date,pay)
        self.animals_under_care = []
        self.max_animals = 20
        self.schedule = {}

    def __str__(self):
        return '**** VET ****' + super().__str__()

    def create_schedule(self):
        '''
        Creates and displays a schedule for the Vet, based on the animals in their care list, and the tasks
        (including surgery, first aid, therapy and health checks) which these animals require.
        Vets work 9am-5pm and each task takes 1 hour.
        :return: prints a schedule for the Vet with times and tasks
        '''
        time_list = ['9:00am','10:00am','11:00am','12:00pm','1:00pm','2:00pm','3:00pm','4:00pm','5:00pm']
        # set up of time list with hourly intervals
        surgery_list = []
        # set up of surgery list, in case any animals under care require surgery
        therapy_list = []
        # set up of therapy list, in case any animals under care require therapy
        first_aid_list = []
        # set up of first aid list, in case any animals under care require first aid
        health_check_list = []
        # set up of health check list. All animals under care require routine health checks
        overflow = []
        # set up of overflow list for extra work
        for animal in self.animals_under_care:
            health_check_list.append(f'{animal.name} health check')
            # all animals require routine health checks and are added to the health check list
            for issue in animal.health_issues:
                if issue.treatment_plan=='surgery':
                    # checks for any animals requiring surgery and adds them to the surgery list
                    surgery_list.append(f'{animal.name} surgery for {issue}')
                elif issue.treatment_plan=='therapy':
                    # checks for any animals requiring therapy and adds them to the therapy list
                    therapy_list.append(f'{animal.name} therapy for {issue}')
                elif issue.treatment_plan=='first_aid':
                    # checks for any animals requiring first aid and adds them to the first aid list
                    first_aid_list.append(f'{animal.name} first aid for {issue}')

        work_list = surgery_list + therapy_list + first_aid_list + health_check_list
        # combines all lists (in order of assumed priority) into one work list

        # Each vet has 9 time slots to fill in a day, depending on the health issues of animals there may be too much
        # or not enough to fill the schedule
        while len(work_list) < 9:
            # if not enough tasks, add ad hoc duties to the end of the work list until 9 tasks are present
            work_list.append('Ad hoc duties')

        while len(work_list) > 9:
            # while there is too much work for one day
            overflow.append(work_list[9])
            # add the 10th item from the work list to the overflow list
            work_list.pop(9)
            # remove the 10h item from the work list
            overflow_str = ''
            for item in overflow:
                overflow_str += f'{item}\n'
            # create a string to list the extra work which could not be scheduled

        # print header for schedule
        print(f'**** {self.name}\'s schedule ****\n')
        # with 9 time intervals and 9 tasks, create dictionary of times and associated tasks and set as Vet's schedule
        self.schedule = dict(zip(time_list, work_list))


        for key, value in self.schedule.items():
            print(f'{key}: {value}')
        # print the details of the schedule (key and value pairs from dictionary)

        if overflow != []:
            # if there is any extra work which could not be scheduled, print the overflow string
            print(f'Extra Work List: \n{overflow_str}')



    def add_animal(self, animal):
        '''
        Method to add an animal to the Vet's animals_under_care list.
        Checks that vet has capacity to take on another animal
        :param animal: object of class: Animal
        :return: if Vet is at capacity: message advising user that animal could not be added
        if Vet not yet reached capacity: message advising user that animal was added to care list
        '''
        if len(self.animals_under_care) < self.max_animals:
            self.animals_under_care.append(animal)
            print(f'{animal} has been added to {self.name}\'s care list')
        else:
            print(f'{self.name} is assigned {self.max_animals} animals and cannot be assigned any more. Please find '
                  f'another staff member to provide care for this animal')


    def perform_health_check(self, animal):
        '''
        Method for Vet to perform routine health check on animal.
        :param animal: Animal object being checked
        :return: printed statement advising user of outcome
        '''
        sick = random.randint(1,10)
        # random number generated for chances of animal either being found unwell or recovering
        if animal.health_status =='perfect' and sick == 1:
        # 10% chance of healthy animal found to have illness
            animal.health_status = 'under treatment'
            # place animal under treatment
            animal.health_issues.append(health_issues.Illness('Measles', 'spotty', 1/1/2025, 'bad'))
            # create health issue and add to animal's health issues
            return(f'{animal.name} has an illness and has been declared under treatment')
            # advise user of illness
        elif animal.health_status == 'perfect' and sick == 2:
            # 10% chance healthy animal found to have injury
            animal.health_status = 'under treatment'
            # place animal under treatment
            animal.health_issues.append(health_issues.Injury('Wound','bloody',1/1/24,'minor'))
            # create health issue and add to animals health issues
            return(f'{animal.name} has an injury and has been declared under treatment')
            # advise user of injury
        elif animal.health_status == 'perfect' and sick == 3:
            # 10% chance healthy animal found to have behavioural issue
            animal.health_status = 'under treatment'
            # place animal under treatment
            animal.health_issues.append(health_issues.Behavioural_Issue('Agrression','Animal hates everyone and is dangerous',1/1/25,'severe'))
            # create health issue and add to animal's health issues
            return(f'{animal.name} has a behavioural issue and has been declared under treatment')
        elif animal.health_status == 'under treatment' and sick > 5:
        # 50% chance an unhealthy animal will be reviewed and declared healthy
            animal.health_status = 'perfect'
            # remove animal from under treatment by changing health status
            animal.health_issues = []
            # clear animal's health issues
            return(f'{animal.name} has been declared healed')
            # advise user of cleared animal
        else:
        # if no change in status:
            return(f'{animal.name} is still {animal.health_status}')

    def perform_surgery(self,animal):
        '''
        Method for Vet to perform surgery on animal.
        :param animal: object of class: Animal having surgery
        :return: printed statement advising user of outcome
        '''
        success  = random.randint(1,10)
        # random number generated for chances of successful surgery
        if success > 3:
        # 70% chance of successful surgery
            animal.health_status = 'perfect'
            return(f'Successful surgery performed on {animal}\n{animal} has been declared healed')
        else:
        # 30% chance of unsuccessful surgery
            return(f'Unsuccessful surgery performed on {animal}\n{animal} remains under treatment')

    def vet_report(self):
        print('\n**** Vets at Zoo ****')
        for staff in Staff.Staff_list:
            if staff.__class__.__name__ == 'Vet':
                print(staff.name)

    def vet_can_care_report(self):
        print('\n**** Vets with Capacity for Additional Animals ****')
        for staff in Staff.Staff_list:
            if staff.__class__.__name__ == 'Vet':
                if len(staff.animals_under_care) < self.max_animals:
                    print(f'{staff.name}: capacity= {self.max_animals - len(staff.animals_under_care)} animals')


class GiftShop(Staff):
    '''
        A class which represents a gift shop worker. Inherits from abstract class Staff.

        Attributes
        ----------
        name : str
            Staff member's full name
        dob : date
            Staff member's Date of birth
        start_date : date
            Staff member's start date with zoo
        pay : float
            Staff member's annual pay
        schedule : dict
            Staff member's schedule

        Methods
        -------

        create_schedule()
        Returns schedule of times and tasks to be done

        open_shop()
        Returns message that staff member has opened shop

        stock_shelves()
        Returns message that staff member has stocked shelves

        clean_shop()
        Returns message that staff member has cleaned shop

        serve_customers()
        Returns message that staff member has served customers

        close_shop()
        Returns message that staff member has closed shop

        '''


    def __init__(self, name, dob, start_date, pay):
        super().__init__(name,dob,start_date,pay)
        self.schedule = {}

    def __str__(self):
        return '**** GIFT SHOP WORKER ****' + super().__str__()

    def create_schedule(self):
        '''
        Method to create schedule of times and tasks to be done
        Schedule is set for all gift shop staff and does not change
        :return: schedule of times and tasks to be done
        '''

        self.schedule = {
            '9:00am': 'Open Shop',
            '10:00am': 'Serve Customers',
            '11:00am':'Stock Shelves',
            '12:00pm': 'Clean Shop',
            '1:00pm': 'Serve Customers',
            '2:00pm': 'Stock Shelves',
            '3:00pm': 'Serve Customers',
            '4:00pm': 'Close Shop',
        }
        # dictionary created as staff member's schedule: static as all gift shop workers have same schedule

        # print header for schedule
        print(f'**** {self.name}\'s schedule ****\n')
        # print the details of schedule (key and value pairs from dictionary created)
        for key, value in self.schedule.items():
            print(f'{key}: {value}')



    def open_shop(self):
        '''
        Method to open gift shop.
        :return: message advising that gift shop has been opened by staff member
        '''
        return f'{self.name} has opened the shop.'

    def stock_shelves(self):
        '''
        Method to stock shelbes.
        :return: message advising that shelves have been stocked by staff member
        '''
        return f'{self.name} has stocked the shelves'

    def clean_shop(self):
        '''
        Method to clean gift shop.
        :return: message advising that gift shop has been cleaned by staff member
        '''
        return f'{self.name} has cleaned the shop.'

    def serve_customers(self):
        '''
        Method to serve customers.
        :return: message advising that customers have been served by staff member
        '''
        return f'{self.name} has served the customers.'

    def close_shop(self):
        '''
        Method to close gift shop.
        :return: message advising that gift shop has been closed by staff member
        '''
        return f'{self.name} has closed the shop.'

