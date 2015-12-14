from collections import OrderedDict

class weapon(object):
    
    def __init__(self):
        
        self.sharpness = 0.0
        self.type = 'default'
        self.weight = 0.0
        self.name='default'
        
        self.ranged = False
        self.ammo = False
        
    def get_attributes(self):
        self.list = OrderedDict([('Name',self.name), 
                     ('Ranged',self.ranged), 
                     ('Ammo',self.ammo),
                     ('Type',self.type), 
                     ('Weight',self.weight),
                     ('Sharpness',self.sharpness)])
        

        return self.list
    
    def print_attributes(self):
        try:
            for i in self.list:
                print"%s:"%i, self.list[i]
            print "\n"
        except AttributeError:
            print "please use get_attributes first"