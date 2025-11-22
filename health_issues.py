import random

class HealthIssue():

    def __init__(self, name, description, date_reported, severity):
        self.name = name
        self.description = description
        self.date_reported = date_reported
        self.severity = severity



    def __str__(self):
        return (f'*** {self.name} ***\n{self.description}\nReported On: {self.date_reported}   Severity:{self.severity}\n')



class Illness(HealthIssue):

    def set_treatment_plan(self):
        treatment_options = ['Wait and see', 'Medication', 'Surgery']
        self.treatment_plan = treatment_options[random.randint(0, len(treatment_options)-1)]



    def __init__(self, name, description, date_reported, severity):
        super().__init__(name,description,date_reported,severity)
        self.set_treatment_plan()

    def __str__(self):
        return 'ILLNESS: ' + super().__str__() + f'Treatment plan: {self.treatment_plan}'

class Injury(HealthIssue):
    def set_treatment_plan(self):
        treatment_options = ['Wait and see', 'First Aid', 'Surgery']
        self.treatment_plan = treatment_options[random.randint(0, len(treatment_options)-1)]

    def __init__(self, name, description, date_reported, severity):
        super().__init__(name,description,date_reported,severity)
        self.set_treatment_plan()

    def __str__(self):
        return 'INJURY: ' + super().__str__() + f'Treatment plan: {self.treatment_plan}'

class Behavioural_Issue(HealthIssue):
    def set_treatment_plan(self):
        treatment_options = ['Wait and see', 'Therapy']
        self.treatment_plan = treatment_options[random.randint(0, len(treatment_options)-1)]

    def __init__(self, name, description, date_reported, severity):
        super().__init__(name,description,date_reported,severity)
        self.set_treatment_plan()

    def __str__(self):
        return 'BEHAVIOURAL ISSUE: ' + super().__str__() + f'Treatment plan: {self.treatment_plan}'




measles = Illness('Measles','gross','1/1/25','bad')
print(measles)
injury2 = Injury('Broken Leg','nasty, nasty','1/2/23','meh')
print(injury2)
bi = Behavioural_Issue('Aggression','bob hates everyone- dangerous to be around','1/1/23','severe')
print(bi)