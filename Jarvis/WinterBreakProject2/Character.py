"""This is the class that will store character information
    including stats, inventory, skills, etc."""

import random
import Weapons

class Character(object):
    """Class that contains the character information. This can
    be used for both enemies and players."""

    def __init__(self, name):
        self.attributes = {"strength": 5,
                           "intelligence": 5,
                           "charisma": 5,
                           "wisdom": 5,
                           "dexterity": 5,
                           "constitution": 5}
        level = 1
        self.xp = 0
        self.hit_dice = "%sd5"%str(self.attributes["constitution"]//4)
        self.health = roll_dice(self.hit_dice)

        self.ac = 10 + roll_dice('1d6')

        self.name = name

        self.inventory = {"rusty dagger": Weapons.RustyDagger(),
                          "Great Sword": Weapons.GreatSword(),
                          "Fists": Weapons.Fists()}

        self.current_weapon = "Great Sword"

    def set_attributes(self, siwdcc):
        """Sets the character's attributes based on the siwdcc tuple input.
        siwdcc = str, int, wis, dex, con, chr"""

        if siwdcc[0] != -1:
            self.attributes["strength"] = siwdcc[0]
        if siwdcc[1] != -1:
            self.attributes["intelligence"] = siwdcc[1]
        if siwdcc[2] != -1:
            self.attributes["wisdom"] = siwdcc[2]
        if siwdcc[3] != -1:
            self.attributes["dexterity"] = siwdcc[3]
        if siwdcc[4] != -1:
            self.attributes["constitution"] = siwdcc[4]
        if siwdcc[5] != -1:
            self.attributes["charisma"] = siwdcc[5]

    def set_health(self, dice_string="2d5"):
        self.health = roll_dice(dice_string)

    def get_standard_character(self, dice_string="3d6"):
        """Uses the standard method for randomly creating a character."""

        attributes = []
        for _ in range(6):
            attributes.append(roll_dice(dice_string))

        self.set_attributes(attributes)

        self.hit_dice = "%sd5"%str(self.attributes["constitution"]//4)
        self.health = roll_dice(self.hit_dice)


    def print_attributes(self):
        """Prints out the attributes in a nice manner."""

        print "%s: \n"%(self.name)
        for att in self.attributes.keys():
            print "%s: %d"%(att.title(), self.attributes[att])
        print "Health: %d"%(self.health)
        print "\n"

    def attack(self, attackee, display_health=False):
        print "%s attacks %s with %s!"%(self.name, attackee.name, self.current_weapon)
        ac_check_roll = roll_dice('1d20')
        if ac_check_roll > attackee.ac:
            damage = roll_dice(self.inventory[self.current_weapon].hit_dice)
            attackee.health -= damage
            print "%s deals %d damage!"%(self.name, damage)
            if display_health:
                print "%s has %d health."%(attackee.name, attackee.health)
            if attackee.health <= 0:
                attackee.die()
        else:
            print "%s misses!"%(self.name)

    def print_short(self):
        print "%s: %d health left"%(self.name, self.health)

    def die(self):
        print "%s dies!"%(self.name)

def roll_dice(string):
    """Based on a string will return a dice roll.
        '4d6' will roll 4 6-sided dice and return the total."""

    nums = string.split('d')
    total = 0
    for _ in range(int(nums[0])):
        total += random.randint(1, int(nums[1]))

    return total
