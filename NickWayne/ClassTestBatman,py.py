class Player(object):

    def __init__(self):
        pass

    def attack(self, attackee):
        if attackee.health <= 0:
            print ("%s is already dead!" %attackee.name)
        else:
            attackee.health -= self.strength
            print ("%s has %i health left" %(attackee.name, attackee.health))

class Batman(Player):

    def __init__(self):
        self.name = 'Batman'
        self.health = 100
        self.strength = 80

class Penguin(Player):

    def __init__(self):
        self.name = 'Penguin'
        self.health = 120
        self.strength = 40

Batman = Batman()
Penguin = Penguin()

Batman.attack(Penguin)
Penguin.attack(Batman)
if Batman.health<=0:
    player="Batman"
elif Penguin.health<=0:
    player="Penguin"
elif Batman.health<=0 or Penguin.health<=0:
    print  player, "is DEAD"
