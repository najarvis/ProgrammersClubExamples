from collections import OrderedDict
import random

global presets
presets = {"Ninja":{"strength":5, "speed":15,"ranged":10, "max_health":100, "magic":10, "mana":20},
            "Knight":{"strength":15, "speed":5, "ranged":10, "max_health":100, "magic":5, "mana":10},
            "Paladin":{"strength":10, "speed":10, "ranged":5, "max_health":100, "magic":10, "mana":20},
            "Archer":{"strength":5, "speed":15, "ranged":15, "max_health":100, "magic":5, "mana":10},
            "Wizard":{"strength":5, "speed":10, "ranged":5, "max_health":100, "magic":15, "mana":30},
            "Beserker":{"strength":15, "speed":10, "ranged":5, "max_health":100, "magic":5, "mana":10}}

class player:
    
    def __init__(self):
        
        for i in presets:       #Lists out classes
            print i
            
        done = False
        while done == False:
            preset = raw_input("Please choose your Class: ").title()        #Lets the player select the class
            if preset in presets:
                done = True
        
        if preset in presets.keys():
            self.attributes= OrderedDict(sorted(presets[preset].items()))   # creates an ordered list sorted alphabetically 
        else:
            self.attributes=0
        
        self.type = preset
        self.level = 1
        self.xp = 0
        self.health = self.attributes["max_health"]
        

    def attack(self, attackee, force):
        print force
        attackee.health-=force*5
        
    def level_up(self, choices):
        print "You can level up:"
        for key in self.attributes.keys():
            print "%s: %d" %(key, self.attributes[key])
        while choices > 0:
            if choices > 1:
                choice = raw_input("%d choices left: "%choices).lower()
            else:
                choice = raw_input("%d choice left: "%choices).lower()
            if choice in self.attributes.keys():
                choices -=1
                if choice == "max health" or choice == "health":
                    self.attributes["max health"]+=10
                    continue
                self.attributes[choice]+=1
        self.health = self.health_max
        self.level +=1
        
class enemy:
    
    def __init__(self, type, rndm=False):
        if rndm:
            x = random.randint(0, len(presets)-1)
            self.attributes= presets[presets.keys()[x]]
            self.type = presets.keys()[x]
        else:
            type = type.title()
            self.attributes= presets[type]
            self.type = type
        self.health = self.attributes["max_health"]
    
    def attack(self, attackee):
        force= self.attributes[max(self.attributes)]
        print max(self.attributes)
        attackee.health-=force*5
        
    def level_up(self):     #makes enemies unable to level up
        pass
    

    
        
a = player()
x = presets.keys()[random.randint(0, len(presets)-1)]
b = enemy(type = x)
players = [a,b]
while a.health > 0 and b.health > 0:
    c_player=players[0]
    a.attack(b, a.attributes[raw_input(": ")])
    b.attack(a)
    print "You have %d health left!"%a.health
    print 'The %s has %d health left!'%(b.type, b.health)