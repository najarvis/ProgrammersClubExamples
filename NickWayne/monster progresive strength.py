import random
class player(object):

    def __init__(self):
        pass
    def attack(self, attackee):
        if attackee.health <= 0:
                print ("%s is already dead!" %attackee.name)
        else:
            attackee.health -= self.strength
            print ("%s has %i health left" %(attackee.name, attackee.health))

class guy(player):

    def __init__(self):
        guy.lvl=1
        guy.health=(lvl*5)+100
        guy.strength=(lvl*3)+3
        
class monster(player):

    def __init__(self):
        monster.strength=lvl*.5 #monster strength
        monster.health=int(100+(35*(mo_st/2)))
        monster.xp_m =int(monster.health+500) #xp gained by killing the monster






option1="y" #define BEFORE loop
gt=0
t_xp=0
xpr=lvl*1750
while True:
    if option1!="n":
        while t_xp>=xpr:                    
            xpr=lvln*1000 
            lvl=lvl+1
            lvln=lvl+1
            print"*" *98
            print "\n\nLVL UP!!! you have reached lvl ", lvl, "you need ", xpr, " xp to advance to lvl ", lvln, "you have ", t_xp, "total xp\n\n"
            print"*" *98
    st=(
    option="y"
    mn=["wolf", "thug", "bear"]
    random.shuffle (mn)
    
    while option1!="n":
        if mohp <1:
            break #had to add a couple breaks
        else:
            hp=(lvl*5)+100
            while hp>0:
                if option=="y":
                    x=[0, 5, 5, 5, 5, 10, 10, 15]
                if lvl> 15 and lvl < 31:
                    x=[10, 10, 10, 15, 15, 20]
                if lvl> 31 and lvl < 45:
                    x=[15, 15, 15, 20, 20, 25]
                if lvl> 45 and lvl < 60:
                    x=[20, 20, 20, 25, 25, 30]
                if lvl> 60 and lvl < 75:
                    x=[25, 25, 25, 30, 30, 35]
                if lvl> 75:
                    x=[30, 30, 30, 35, 35, 40]
                random.shuffle (x)
                pl_dm=int(st*1.25+x[0])
                mo_dm=int(lvl+mo_st)+ x[0]
                hp=int(hp-mo_dm)
                hp_bd=int(hp+mo_dm) 
                mohp=int(mohp-pl_dm)
                mohp_bd=mohp+pl_dm
                lvln=lvl+1
                g=int(hp/2)
                if mohp<1:
                    gt=gt+g
                    print "you have killed the ", mn[0], "and have received ", g, " gold and recieve ", xp_m, "xp"
                    t_xp=t_xp+xp_m
                    print "you have ", gt, "gold total and ", t_xp, "total xp"
                    option1= raw_input ("\natack again? enter r: ")
                    break
                else:
                    if hp<1: # yolo! XD
                        print "\n\nmohp=", mohp
                        print "hp= 0"
                        print "you have died!"
                        print "total xp= ", t_xp
                    if hp>1: 
                        print "\n\nmohp=", mohp_bd
                        print "hp=", hp_bd
                        print "xp till next lvl= ", xpr
                        print "you dealt ", pl_dm, "damage to the ", mn[0], " who has ", mohp, "hp left"
                        print "you have", hp, "hp after the", mn[0], "dealt",  int(mo_dm), "dammage, "
                        option= raw_input ("\natack again? y/n: ")
                        if option=="n":    #if i didn't add this it would never end but never do anything
                            break
