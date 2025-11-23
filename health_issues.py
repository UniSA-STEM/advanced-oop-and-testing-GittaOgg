"""
File: health_issues.py
Description: Health Issues module for advanced programming assignment containing HealthIssue class and children
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""


import random
from abc import ABC, abstractmethod

class HealthIssue(ABC):
    '''
    A class which represents an animal's health issue, for Illness, Injury and BehaviourIssue classes to inherit from

    Attributes
    ----------
    name: str
        Name of health issue
    description: str
        Description of health issue
    date_reported: date
        Date health issue was reported
    severity: str
        Severity of health issue

    Methods
    -------
    set_treatment_plan():
        abstract method for children to inherit from

'''


    def __init__(self, name, description, date_reported, severity):
        self.name = name
        self.description = description
        self.date_reported = date_reported
        self.severity = severity



    def __str__(self):
        return (f'*** {self.name} ***\n{self.description}\nReported On: {self.date_reported}   Severity:{self.severity}\n')

    @abstractmethod

    def set_treatment_plan(self):
        pass




class Illness(HealthIssue):
    '''
    A class which represents an Illness- one possible animal health issue. Inherits from abstract class HealthIssue

    Attributes
    ----------
    name: str
        Name of health issue
    description: str
        Description of health issue
    date_reported: date
        Date health issue was reported
    severity: str
        Severity of health issue
    treatment_plan: str
        Plan of treatment, chosen at random from Illness treatment options

    Methods
    -------
    set_treatment_plan():
        returns treatment plan for illness

    '''


    def set_treatment_plan(self):
        '''
        A method to choose and set a treatment plan for the illness
        :return: treatment plan
        '''
        treatment_options = ['Wait and see', 'Medication', 'Surgery']
        # set the illness's treatment plan as a random choice from the available options
        self.treatment_plan = treatment_options[random.randint(0, len(treatment_options)-1)]


    def __init__(self, name, description, date_reported, severity):
        super().__init__(name,description,date_reported,severity)
        self.set_treatment_plan()

    def __str__(self):
        return 'ILLNESS: ' + super().__str__() + f'Treatment plan: {self.treatment_plan}'

class Injury(HealthIssue):
    '''
    A class which represents an Injury- one possible animal health issue. Inherits from abstract class HealthIssue

    Attributes
    ----------
    name: str
        Name of health issue
    description: str
        Description of health issue
    date_reported: date
        Date health issue was reported
    severity: str
        Severity of health issue
    treatment_plan: str
        Plan of treatment, chosen at random from Injury treatment options

    Methods
    -------
    set_treatment_plan():
        returns treatment plan for Injury

    '''

    def set_treatment_plan(self):
        '''
        A method to choose and set a treatment plan for the injury
        :return: treatment plan
        '''
        treatment_options = ['Wait and see', 'First Aid', 'Surgery']
        self.treatment_plan = treatment_options[random.randint(0, len(treatment_options)-1)]

    def __init__(self, name, description, date_reported, severity):
        super().__init__(name,description,date_reported,severity)
        self.set_treatment_plan()

    def __str__(self):
        return 'INJURY: ' + super().__str__() + f'Treatment plan: {self.treatment_plan}'

class Behavioural_Issue(HealthIssue):
    '''
    A class which represents a behavioural issue- one possible animal health issue. Inherits from abstract class HealthIssue

    Attributes
    ----------
    name: str
        Name of health issue
    description: str
        Description of health issue
    date_reported: date
        Date health issue was reported
    severity: str
        Severity of health issue
    treatment_plan: str
        Plan of treatment, chosen at random from behavioural issue treatment options

    Methods
    -------
    set_treatment_plan():
        returns treatment plan for behavioural issue

    '''

    def set_treatment_plan(self):
        '''
        A method to choose and set a treatment plan for the behavioural issue
        :return: treatment plan
        '''
        treatment_options = ['Wait and see', 'Therapy','Medication']
        self.treatment_plan = treatment_options[random.randint(0, len(treatment_options)-1)]

    def __init__(self, name, description, date_reported, severity):
        super().__init__(name,description,date_reported,severity)
        self.set_treatment_plan()

    def __str__(self):
        return 'BEHAVIOURAL ISSUE: ' + super().__str__() + f'Treatment plan: {self.treatment_plan}'




