import random

class batman (object):

	def __init__(self):
		self.power = 100000
		self.defence = 100000
		self.power = 100
	def attack(self, victim):
		victim.health -= self.power
		print "%s took %d damage!" % (victim.name, self.power)
		print "%s has %d health left!" % (victim.name, victim.health)

class goon(object):
    
    def __init__(self, name):
        self.power = 100
        self.defence = 0
        self.health =1000
        self.name = name

attack = True
while attack ==True:
    bman = batman()
    goon1 = goon("ricky")
if input == 1:
    bman.attack(goon1)
if input == 2:
    rand = random.randint(1,3)
    if rand == 1:
        bman.attack(goon1)
    elif rand == 2:
        bman.attack(goon1)
        goon1.attack(bman)
    else:
        goon1.attack(bman)
