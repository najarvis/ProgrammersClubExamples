import pprint
from collections import OrderedDict
from Player import player
from Weapon import weapon
import sys
        
print "Welcome To Fallen Warriors Alpha!\n"

try:
    if sys.argv[1] == '-godmode':
        main_player = player('')
        main_player.name = 'GODMODE'
        main_player.strength = 100
        main_player.speed = 100
        main_player.magic = 100
        main_player.agility = 100
        main_player.ranged = 100
        main_player.block = 100
        main_player.sword = 100
        main_player.blunt = 100
        
        main_player.xp = 0
        main_player.level = 801
    
    else:
        name = ''
        while name== '':
            name = raw_input("Enter thy name?: ")
    
            print '\n'

        main_player = player(name)      
        
except Exception:
    name = ''
    while name== '':
        name = raw_input("Enter thy name: ")
    
        print '\n'

    main_player = player(name)

print 'Welcome %s!'%main_player.name
actions = ['Mission', 'Train', 'Rest', 'Shop', 'Stats', 'Inventory']

while True:
    print "What would you like to do?"
    for i in actions:
        if i == actions[-1]:
            print "or %s."%i
        else:
            print "%s,"%i,
    print "\n"
    
    choice = raw_input(': ').title()
    print "\n"
    if choice in actions:
        
        if choice == 'Stats':
            main_player.get_attributes()
            main_player.print_attributes()
            

    else:
        print "please choose a valid choice"
