import random

class unit(object):

    def __init__():
        self.speed = 0
        self.strength = 0
        self.dps = 0
        self.health = 0
        self.defence = 0

    def attack(self, attackee):
        if random.randint(0, 100) <= attackee.speed*10:
            print "Evades!"
        else:
            attackee.health -= (self.strength*self.dps)/attackee.defence
            print self.team + " Attacks " + attackee.team + " and deals " + str((self.strength*self.dps)/attackee.defence) + " damage."
            print attackee.team + " has " + str(attackee.health)

        
class light(unit):

    def __init__(self, team):
        self.team = team
        self.speed = 8.5
        self.strength = 4
        self.dps = 10
        self.health = 10000
        self.defence = 2

class medium(unit):

    def __init__(self, team):
        self.team = team
        self.speed = 5
        self.strength = 7
        self.dps = 8
        self.health = 10000
        self.defence = 5

class heavy(unit):

    def __init__(self, team):
        self.team = team
        self.speed = 2.5
        self.strength = 10
        self.dps = 5
        self.health = 10000
        self.defence = 9

class jarvis(unit):

    def __init__(self, team):
        self.team = team
        self.speed = 0
        self.strength = 1e+100
        self.dps = 500
        self.health = 10000
        self.defence = 9001

unit_dict = {'light':light('a'), 'medium':medium('a'), 'heavy':heavy('a'), 'jarvis':jarvis('a')}
for i in unit_dict.keys()[:-1]:
    print i.upper()

Jarvis = unit_dict[raw_input("What tank do you wanna be? " ).lower()]
Jarvis.team = (raw_input("what do you want to be called? ").lower())
Noah = unit_dict[raw_input("What tank do you wanna be? " ).lower()]
Noah.team = (raw_input("what do you want to be called? ").lower())


ap = Jarvis
dp = Noah
ep = Noah

while Jarvis.health > 0 and Noah.health > 0:
    
    ap.attack(dp)
    dp = ap
    ap = ep
    ep = dp

raw_input()
