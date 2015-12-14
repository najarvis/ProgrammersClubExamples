class player(object): #the base class uses object in the parentheses.
                        #in this class you will define the functions every player has

    def __init__(self): #Here you initialise the class. since it has no attribute we use 'pass'
        pass

    def attack(self, attackee): #here we make a function that each player (warrior, mage, etc.) can use
        if attackee.health <= 0:
            print ("%s is already dead!" %attackee.name)
        else:
            attackee.health -= self.strength
            print ("%s has %i health left" %(attackee.name, attackee.health))


class warrior(player): #here we define a class the derives from 'player' it has all the functions 'player' has

     def __init__(self): #we initialize the class and define it's attributes
          self.name= 'warrior'
          self.health= 100
          self.strength=150

                          #any special functions would go here

class mage(player): #Same as before

     def __init__(self, name): #same as before except i added name which i will explain later
          self.name= name
          self.health= 1500
          self.strength= 1e+10
          
warrior= warrior()    #here we call the class into existance.
mage= mage('Nick the magic sexy beast')            #if the name wasn't predetermined you would put it's name in the parenthesis like i do here

warrior.attack(mage) #now we call a function 'warrior(who's doing the action).attack(what he's doing)(mage)(who he's doing his action on)
mage.attack(warrior)
               
