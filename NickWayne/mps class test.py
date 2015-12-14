import time
import random
option2=raw_input("do you want to run through? y/n: ").lower()
option=raw_input("what is your name? ")
option1=raw_input("what is the monsters name? ")
pv=random.randint(0, 20)
mv=random.randint(0, 15)

while True:
    if option2=="y":
        class player(object):

            def __init__(self):
                pass
            
            def attack(self, attackee):
                if attackee.health <= 0:
                        print ("%s is already dead!" %attackee.name)
                else:
                    attackee.health -= self.strength
                    print ("%s has %i health left" %(attackee.name, max(attackee.health, 0)))
                    time.sleep(.15)
            def battle(self, attackee):
                while True:
                    t_xp=guy.t_xp
                    if guy.health>=1 and monster.health>=1:
                        guy.attack(monster)
                        time.sleep(.15)
                        pv=random.randint(0, 20)
                    else:
                        if guy.health<=0:
                            print "%s has been killed!" %(guy.name)
                            option2=raw_input("play again? y/n: ")
                            if option2=="y":
                                guy.health=(guy.lvl*5)+100
                                monster.health=100+(35*(monster.strength-mv)/2)
                                break
                        elif monster.health<=0:
                            print "%s has been killed!" %(monster.name)
                            guy.get_TotalXP(guy.t_xp, monster.xp_m) #Call the function to get total XP when monster is killed
                            print t_xp
                            option2=raw_input("play again? y/n: ")
                            if option2=="y":
                                guy.health=(guy.lvl*5)+100
                                monster.health=100+(35*(monster.strength-mv)/2)
                                break
                    if guy.health>=1 and monster.health>=1:
                        monster.attack(guy)
                        mv=random.randint(0, 15)
                    else:
                        if guy.health<=0:
                            print "%s has been killed!" %(guy.name)
                            option2=raw_input("play again? y/n: ")
                            if option2=="y":
                                guy.health=(guy.lvl*5)+100
                                monster.health=100+(35*(monster.strength-mv)/2)
                                break
                        elif monster.health<=0:
                            print "%s has been killed!" %(monster.name)
                            guy.get_TotalXP(guy.t_xp, monster.xp_m) #Call the function to get total XP when monster is killed
                            print t_xp
                            option2=raw_input("play again? y/n: ")
                            if option2=="y":
                                guy.health=(guy.lvl*5)+100
                                monster.health=100+(35*(monster.strength-mv)/2)
                                break
        class guy(player):

            def __init__(self):
                guy.name= option
                guy.lvl=1
                guy.health=(guy.lvl*5)+100
                guy.strength=(((guy.lvl*3)+3)*1.25)+pv
                guy.t_xp=0
                
            def get_TotalXP(t_xp, xp_m): #uses a function to get the total XP instead of defineing it (Which only happens once)
                t_xp += xp_m

        class monster(player):

            def __init__(self, lvl):
                monster.name=option1
                monster.strength=(guy.lvl*.75+mv)#monster strength
                monster.health=100+(35*(monster.strength-mv)/2)
                monster.xp_m =(monster.health+500) #xp gained by killing the monster, don't set it to 0
                 
        guy=guy()
        monster=monster(guy.lvl)
        lvl=guy.lvl
        guy.battle(monster)
        
