from collections import OrderedDict

class player(object):
    def __init__(self, name):
        self.name = name
        
        self.strength = 5
        self.speed = 5
        self.agility = 5
        self.magic = 5
        self.mana = 50
        self.ranged = 5
        self.block = 5
        self.sword = 5
        self.blunt = 5
        self.current_weapon = 'UNARMED'
        
        self.xp = 0
        self.level =1
        
        self.inventory = []
        
    def get_attributes(self):
        self.att = OrderedDict([('Level', self.level),
                    ('Experience', self.xp),
                    ('Speed', self.speed),
                    ('Strength', self.strength),
                    ('Agility', self.agility),
                    ('Ranged', self.ranged),
                    ('Block', self.block),
                    ('Blunt', self.blunt),
                    ('Sword', self.sword),
                    ('Magic', self.magic),
                    ('Mana', self.magic),
                    ('Current Weapon', self.current_weapon)])

        
        return self.att
    
    def print_attributes(self):
        try:
            for i in self.att:
                print"%s:"%i, self.att[i]
                if i == 'Experience':
                    print "\n"
            print "\n"
        except AttributeError:
       
            print "please use get_attributes first"