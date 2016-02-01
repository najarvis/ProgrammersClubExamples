class Weapon(object):

    def __init__(self, hd='1d3'):
        self.hit_dice = hd

class RustyDagger(Weapon):

    def __init__(self):
        Weapon.__init__(self, '1d4')

class ShortSword(Weapon):

    def __init__(self):
        Weapon.__init__(self, '1d8')

class Staff(Weapon):
    
    def __init__(self):
        Weapon.__init__(self, '1d6')

class GreatSword(Weapon):

    def __init__(self):
        Weapon.__init__(self, '2d6')

class Fists(Weapon):

    def __init__(self):
        Weapon.__init__(self)
