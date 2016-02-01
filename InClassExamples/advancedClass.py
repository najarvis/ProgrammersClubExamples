"""This is designed to teach a more advanced topic of classes, superclasses!
   (and of course we will accomplish this by using our favorite superhero!)
   """

class Entity(object):
	"""This class will be the 'super' class. It defines in a broad sense how
	   the other classes behave and provides more or less a template."""

	def __init__(self, name):
		"""This initialization method assignes variables to all subclasses,
		   so only put here what you want for all of them! We make 'name'
		   a parameter so we won't have to edit any of Goon's code and we
		   can keep the code short."""

		self.power = 100  #Set some default values
		self.health = 100 #that may or may not be overwritten
		self.name = name

	def attack(self, victim):
		"""This function will be used to attack another initialized class,
		   whether it be another batman or a goon. Takes health away from
		   the victim equal to the power of the one attacking. 

		   Because it is in a superclass, we only need to define it once,
		   the subclasses will inherent this automatically and can use it
		   just as if we had defined it explicitly."""
			
		print "%s attacks %s!" %(self.name, victim.name) #https://docs.python.org/2/library/string.html#format-specification-mini-language (description of string formatting)
		victim.health -= self.power
		print "%s took %d damage!" % (self.name, self.power)
		print "%s has %d health left!" % (self.name, victim.health)
		print "" #Here I print a blank line so it is easy to see where the attack ends.

class Batman(Entity):
	"""This is the first subclass (also known as a 'child'). Notice how instead of 'object'
	   we put 'Entity'? This is how we tell the computer we want Batman to be a subclass of
	   the Entity class."""

	def __init__(self):
		"""This method will be called when Batman is initialized
		   (the 'bman = Batman()' below). 
		
		   The 'Entity.__init__(self, "Batman")' can be broken down into a couple
		   of steps.
		   1. The 'Entity' means we are referring to the superclass that we specified
		      before
		   2. The '__init__()' means we are calling the initialization function of
		      the superclass. This will give batman all of the default values and
		      functions that Entity has.
		   3. The "Batman" will make sure that 'name' is always set to "Batman."
		"""
 
		Entity.__init__(self, "Batman")
		self.power = 100000 #Here because we don't want the default power level for batman,
				    #we overwrite the value to what we want (in this case: 100000).
	
class Goon(Entity):

	def __init__(self, name):
		"""Same as before, however notice how we do not pass "Batman" into the initializtion
		   function. This means that we want to specify the names when we create the Goon."""

		Entity.__init__(self, name)
		self.power = 10 #We still do not want the default power level, so we overwrite it.
	
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
