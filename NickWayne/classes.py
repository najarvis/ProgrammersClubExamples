import random

class Tank(object):

    def __init__(self, tank_type):
        self.ammo = tank_type.ammo
        self.tank_type = tank_type

    def fire(self, Tank2):
        if self.ammo >= 1 or Tank2.armor >0:
            self.ammo -= 1
            print ("The %s tank fires at the %s tank!" % (self.tank_type, Tank2.tank_type))
            hit = random.randint(0, 100)
            if hit <= self.accuracy:
                print "Hit!"
                Tank2.armor -= self.damage
                print ("The %s tank has %i armor left!" % (Tank2.tank_type, max(Tank2.armor, 0)))
                Tank2.state = 'Fired At'
                if Tank2.armor<0:
                    Tank2.explode(Tank2.tank_type)
                else:
                    Tank2.fight_back(self)
            else:
                print "Miss!"
        return self.ammo, Tank2.armor

    def explode(self, tank_type):
        print ("%s explodes!" %tank_type)
        self.state = 'DEAD'
        

    def fight_back(self, attacker):
        if self.state == 'Fired At':
            self.fire(attacker)

class Laser_Tank(Tank):

    def __init__(self, name):
        self.name = name
        self.tank_type = 'Laser'
        self.ammo = 5
        self.accuracy = 90
        self.armor = 50
        self.damage = 60
        self.state = 'Alive'

class Heavy_Tank(Tank):

    def __init__(self, name):
        self.name = name
        self.tank_type = 'Heavy'
        self.ammo = 20
        self.accuracy = 40
        self.armor = 150
        self.damage = 100
        self.state = 'Alive'

class Light_Tank(Tank):

    def __init__(self, name):
        self.name = name
        self.tank_type = 'Light'
        self.ammo = 10
        self.accuracy = 80
        self.armor = 40
        self.damage = 40
        self.state = 'Alive'

class Round(object):

    def __init__(self):
        self.type = ''
        self.speed = 0.

Tank1 = Laser_Tank("Warrior")
Tank2 = Heavy_Tank("Destroyer")
Tank3 = Light_Tank("Panther")
Alive_Tanks = [Tank1, Tank2, Tank3]

while len(Alive_Tanks) > 1:
    
    x = random.randint(0, len(Alive_Tanks)-1)
    y = random.randint(0, len(Alive_Tanks)-1)
    while y == x:
        y = random.randint(0,len(Alive_Tanks)-1)
    Alive_Tanks[x].fire(Alive_Tanks[y])
    if Alive_Tanks[y].state == 'DEAD':
        del Alive_Tanks[y]

    if len(Alive_Tanks) == 1:
        print Alive_Tanks[0].tank_type, "is the winner"
        raw_input("")

