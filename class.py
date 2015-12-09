"""This program is designed to teach basic classes by using everyone's favorite
   superhero, Batman."""

class Batman(object):
	"""First we create a class for Batman himself. Don't worry about the 'object',
	   it isn't very important but you should get used to using it."""

	def __init__(self):
		"""This method will be called when Batman is initialized
		   (the 'bman = Batman()' below). We set the values of
		   power, health, and name"""

		self.power = 100000
		self.health = 100
		self.name = "Batman"
	
	def attack(self, victim):
		"""This function will be used to attack another initialized class,
		   whether it be another batman or a goon. Takes health away from
		   the victim equal to the power of the one attacking."""
			
		print "%s attacks %s!" %(self.name, victim.name) #https://docs.python.org/2/library/string.html#format-specification-mini-language (description of string formatting)
		victim.health -= self.power
		print "%s took %d damage!" % (self.name, self.power)
		print "%s has %d health left!" % (self.name, victim.health)

class Goon(object):
	"""This class will be for random enemies, people specifically ones that are NOT Batman.
	   Does basically everything the Batman does."""

	def __init__(self, name):
		"""This is the same as before except we pass an additional argument: 'name',
		   letting us name each enemy when we create it."""

		self.power = 10
		self.defence = 3
		self.health = 100
		self.name = name
	
	def attack(self, victim):
		print "%s attacks %s!" % (self.name, victim.name)
		victim.health -= self.power
		print "%s took %d damage!" % (self.name, self.power)
		print "%s has %d health left!" % (self.name, victim.health)

#Here we create 1 instance of Batman and 3 instances of Goon (each named differently).
bman = Batman()
person1 = Goon("Tom")
person2 = Goon("Nick")
person3 = Goon("Bjorn")

#Batman attacks person 1, then person 2 gets the jump on him, then Batman wrecks the two
#in a sick combo move.
bman.attack(person1)
person2.attack(bman)
bman.attack(person2)
bman.attack(person3)

"""
student1 = Goon("Logan")
student2 = Goon("Caleb")

student1.attack(student2)
student2.attack(student1)
"""
