"""
File: main.py
Description: Main module for running advanced programming assignment
Author: Natasha Hunter
ID: 110439590
Username: hunny006
This is my own work as defined by the University's Academic Integrity Policy.
"""


import animal
import enclosure
import staff
import health_issues

# set up animals
r1 = animal.Reptile('Andrew',10,'perfect','Lizard','Bugs')
m1 = animal.Mammal('Elizabeth',3,'perfect','Tiger','meat')
b1 = animal.Bird('George',4,'perfect','Cockatoo','Bugs')

# set up staff
zk1= staff.Zookeeper('Joe Bloggs',1/1/2023,1/1/25,60000)
v1 = staff.Vet('Fiona Mertens',1/1/1980,1/1/2024,100000)
gs1 = staff.GiftShop('Barry Jones',1/1/1990,1/1/2020,40000)

# set up enclosures
e1 = enclosure.Enclosure('Jungle1','Medium','Jungle')
e2 = enclosure.Enclosure('Aviary1','Large','Aviary')
e3 = enclosure.Enclosure('Arctic1','Small','Arctic')

# add animals to enclosures
e1.add_animal(m1)
e2.add_animal(b1)
e3.add_animal(r1)


# add all enclosures to zookeeper's list
zk1.add_enclosure(e1)
zk1.add_enclosure(e2)
zk1.add_enclosure(e3)

# add all animals to zookeeper's list
zk1.add_animal(r1)
zk1.add_animal(m1)
zk1.add_animal(b1)

# add all animals to vet's list
v1.add_animal(r1)
v1.add_animal(m1)
v1.add_animal(b1)

# create schedules for the Gift Shop worker and the vet
gs1.create_schedule()
v1.create_schedule()


# vet perform health checks
v1.perform_health_check(r1)
v1.perform_health_check(m1)
v1.perform_health_check(b1)

# display some animal reports
animal.Reptile.reptile_report(r1)
animal.Bird.bird_treatment_report(b1)

# display some staff reports
staff.Zookeeper.zookeeper_can_feed_report(zk1)
staff.Vet.vet_report(v1)

# display some enclosure reports
enclosure.Enclosure.enclosure_capacity_report(e1)
enclosure.Enclosure.enclosure_cleanliness_report(e1)
