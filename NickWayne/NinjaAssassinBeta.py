print "-" *75
print "                                 NINJA ASSASSIN BETA v. 1.0.1                          "
print "-" *75

import random
import cPickle
import os
import SPT
import Spells


option2 = 1
option = 1

while True:
    if option2 == "N" or option == "N":
        break
    if option2 == "Y" or 1:        
        a=1
        weapons = ['Fists', 'Test']
        bw = 0
        bmw = 0
        xp = 0
        ww = weapons[0]
        mana = 10
        f = 0
        b = 0
        spell_lvl = 0
        pm = 1
        EB = 1
        CP_T = 1
        cost = 0
        CP = 0
        hr = 15
        gold = 20
        weapon = 1
        ninja = 1
        hp = 100
        magic = 1
        work1 = 1
        EHP=4000
        day = 1
        potion = 0
        sign = 1

        Fireball = {'name': 'Fireball', 'power' : 5, 'mana': 10, 'skill_level': 1, 'cost': 0}

        Iceball = {'name': 'Iceball', 'power': 7, 'mana': 15, 'skill_level': 3, 'cost': 20}

        Bolt = {'name': 'Bolt', 'power': 10, 'mana': 21, 'skill_level': 6, 'cost': 35}

        Leech = {'name': 'Leech', 'power': ninja*.75, 'mana': 25, 'skill_level': 10, 'heal': ninja*.75, 'cost': 100}

        Heal = {'name': 'Heal', 'power': 0, 'mana': 15, 'skill_level': 5, 'heal': 15, 'cost': 50}

        World_Destroyer = {'name': 'World Destroyer', 'power': 100, 'mana': 150, 'skill_level': 50, 'cost': 500}

        Shurikin = {'name': 'Shurikin'} 

        Spell_List = ['Fireball']
        Spell_List2 = [Fireball]

        PossibleSpell_List = ['Fireball', 'Iceball', 'Bolt', 'Leech', 'Heal', 'World Destroyer']
        PossibleSpell_List2 = [Fireball, Iceball, Bolt, Leech, Heal, World_Destroyer]



        option = raw_input("N to start a new game, Q to quit, L to load, Or type H for help: ")
        if option == "H":
            print "If something has a letter next to it such as the\nH you typed in to get here, type that one letter\nto access that option. If two letters have a / between\nthem, just type one letter; such as the Y/N at the top.\nThat just means Yes/No. Got it?\n"
            print "The stores are a little different.\nyou have to type in the NUMBER\n to buy it.\n"
            print "You have 15 hrs each day to do what you need to do.\ngoing on a mission takes 5 hrs. buying something takes 1 hr.\ntraining takes 2 hrs.\n"
            print "You can fight the Samuri King once you are level 75.\n"
            print "To cast a spell type the number before the spell.\n"
            print "There are still a few bugs/glitches but nothing major.\n"
            print "BTW if you try to create your own spell it wont have any power\n"

        elif option == "Q":
            break
        elif option == "N" or option=="L":

            if option == "N":
                print "The goal of the game is to defeat\nthe Samuri King within 50 days."
                
                print "\nWere you born under the sign of"
                while a==1:
                    sign = raw_input("the warrior or mage? W/M: ")
                    print ""
                    if sign == "W":
                            weapon = 25
                            
                            print "your weapon level is",weapon,"."
                            
                            print "your magic level is",magic,". You have",mana,"mana."
                            
                            print "you have the spell Fireball."
                            a=0
                            b=1
                            raw_input("")
                            
                    elif sign == "M":
                            magic = 25
                            mana = 30
                            pm = 30
                            Spell_List.append('Iceball')
                            Spell_List2.append(Iceball)
                            print "your magic level is",magic,". You have",mana,"mana."
                            
                            print "you have spells",
                            for x in range(0, len(Spell_List)):
                                if x == len(Spell_List)-1:
                                    print Spell_List[x] + "."
                                else:
                                    print Spell_List[x] + ", ",
                            print "your weapon level is",weapon,"."
                            a=0
                            b=1
                            raw_input("")
                    else:
                            print "That is not a valid answer!"
                    os.system('cls')
                            
            elif option == "L":
                try:
                    file=open("NinjaAssassinSave.py", 'rb')
                    E = cPickle.load(file)
                    spell = E[0]
                    weapons = E[1]
                    M_weapons = E[2]
                    mw=E[3]
                    bmw=E[4]
                    bw=E[5]
                    ww=E[6]
                    mana=E[7]
                    f=E[8]
                    hr=E[9]
                    pm=E[10]
                    EB=E[11]
                    CP_T=E[12]
                    CP=E[13]
                    gold=E[14]
                    weapon=E[15]
                    ninja=E[16]
                    hp=E[17]
                    magic=E[18]
                    day=E[19]
                    potion=E[20]
                    xp=E[21]
                    b=1
                except Exception:
                    print "Save file not found!"
                    raw_input("please restart the program: ")
                    break
                    
            while hp > 0 or EHP > 0 or day < 50:
                if hp <= 0:
                    print "Game over"
                    break
                elif hp > 0:
                    if EHP <= 0:
                        print "you killed the Samuri King!!!! YOU WIN!!!!!"
                        x=raw_input("congrats, press enter to quit.")
                        break
                    elif EHP > 0:
                        if day >= 50:
                            print "The Samuri King has found your camp and sends thousands of Samuri to kill you, Game Over!!!"
                            break
                        elif day < 50:
                            items = [15, 20, 25, 30, 35, 40, 45, 50, 50, 50, 75, 80, 90, 100, 100]
                            random.shuffle(items)
                            x = items[2]
                            items2 = [0, 1, 2, 3]
                            random.shuffle(items2)
                            y = items2[2]
                            items3 = [5, 10, 15, 11, 13, 17, 7, 21, 25, 27, 30]
                            random.shuffle(items3)
                            z = items3[2]
                            monster = ["skeleton", "samuri", "angry farmer", "large rat", "strange green guy", "Carrot", "Zombie", "Priest", "Rouge Ninja", "Super Mario", "Yoshi"]
                            random.shuffle(monster)
                            mo = monster[2]

                            while xp >= 10 * (1.25 ** (ninja - 1)):
                                print "LEVEL UP!"
                                ninja = ninja + 1
                                print "Your level is now", ninja, "\n"
                            
                            print "it is day",day,". You have",hr,"hours left. You have", hp, "health left"

                            
                            print ""
                            work1 = raw_input ("---------------\n1 to train\n2 to go on a mission\n3 to rest\n4 to shop\n5 for inventory\n6 to save\n7 to load\n8 to Quit\n---------------\n: ")
                            print ""
                            os.system('cls')
                            if work1 == "1":
                                if hp <= 25:
                                    print "you do not have enough hp"
                                if hp > 25:
                                    which = raw_input("do you want to train magic (M) or weapon (W) or 0 to exit ")
                                    if which == "M":
                                        mana1 = raw_input("Do you want to train with a trainer for 20 gold or by yourself? T/Y ")
                                        if mana1 == "T":
                                            if gold < 20:
                                                print "not enough gold."
                                            if gold >= 20:
                                                if hr < 2:
                                                    print "not enough time left."
                                                if hr >= 2:
                                                    gold = gold - 20
                                                    magic = magic + 5
                                                    mana = mana + 3
                                                    pm = pm + 3
                                                    xp = xp + 25
                                                    hp = hp - 20
                                                    hr = hr - 2
                                                    print "you now have",gold,"gold"
                                                    
                                                    print "your magic level is now",magic,". You have",mana,"mana."
                                                    
                                                    print "you are now level",ninja,"."
                                                    
                                                    print "you now have",hp,"hp"
                                                    
                                        if mana1 == "Y":
                                            if hr < 2:
                                                print "not enough time left."
                                            if hr >= 2:
                                                magic = magic + 1
                                                mana = mana + 1
                                                xp = xp + 10
                                                pm = pm + 1
                                                print "Your magic level is now",magic,". You have",mana,"mana."
                                                
                                                print "your level is now",ninja,"."
                                                
                                                hr = hr - 2
                                    if which == "W":
                                        sword = raw_input("do you want to train with a trainer for 20 gold or by yourself? T/Y ")
                                        if sword == "T":
                                            if gold < 20:
                                                print "not enough gold."
                                            if gold >= 20:
                                                if hp <= 25:
                                                    print "not enough gold."
                                                if hp > 25:
                                                    gold = gold - 20
                                                    weapon = weapon + 5
                                                    xp = xp + 30
                                                    hp = hp - 25
                                                    hr = hr - 2
                                                    print "you now have",gold,"gold"
                                                    
                                                    print "your weapon level is now",weapon,"."
                                                    
                                                    print "you are now level",ninja,"."
                                                    
                                                    print "you now have",hp,"hp"
                                                    
                                        if sword == "Y":
                                            if hp <= 25:
                                                print "not enough gold."
                                            if hp > 25:
                                                weapon = weapon + 1
                                                xp = xp + 10
                                                hp = hp - 25
                                                print "Your weapon level is now",weapon,"."
                                                
                                                print "Your level is now",ninja,"."
                                                
                                                print "You now have",hp,"hp"
                                                
                                                hr = hr - 2
                            if work1 == "2":
                                if ninja >= 75:
                                    last = raw_input("do you want to face the samuri king (S)or go on a normal mission (N)?: ")
                                    if last == "S":
                                        while EHP > 0:
                                            samuri = [0, 25, 40, 40, 50, 50, 50, 50, 50, 50, 50, 80, 80, 80, 100, 100, 150, 200]
                                            random.shuffle(samuri)
                                            sam = samuri[2]
                                            attack = [0, 1, 1, 1, 2, 3]
                                            random.shuffle(attack)
                                            a = attack[2]
                                            fight = raw_input ("do you wish to use melee (A), use magic (M), or use a potion (P): ")
                                            if fight == "A":
                                                EHP = EHP - weapon * a * 5
                                                hp = hp - sam
                                                
                                                print "You dealt", weapon * a * 5,"damage, using your",ww
                                                
                                                print "The samuri king has",EHP,"health left."
                                                
                                                print "You took", sam, "damage from the samuri king"
                                                
                                                print "you have",hp,"hp left."
                                                                  
                                            elif fight == "P":
                                                if potion >= 1:
                                                    potion = potion - 1
                                                    hp = hp + 100
                                                    
                                                    print "You now have", potion,"potions"
                                                    
                                                    print "You now have",hp,"hp."
                                                    
                                                    hp = hp - sam
                                                    print "You took",sam,"damage from the samuri king."
                                                    
                                                elif potion < 1:
                                                    print "You do not have any potions"
                                                    
                                            elif fight == "M":
                                                print spell
                                                sattack = input("what spell do you want to use?: ")
                                                if mana - sattack < 0:
                                                    print "not enough mana."
                                                elif mana - sattack >= 0:
                                                    EHP = EHP - sattack * a * (magic / 5)
                                                    hp = hp - sam
                                                    mana = mana - sattack
                                                    
                                                    print "You dealt", sattack * a * (magic / 5), "damage, using your",mw,"."
                                                    
                                                    print "The samuri king has",EHP, "health left."
                                                    
                                                    print "You took",sam, "damage from the Samruri King."
                                                    
                                                    print "You have",hp,"hp. You have",mana,"mana."
                                                    
                                            if EHP <= 0:
                                                pass
                                            
                                                break
                                        
                                    if last == "N":
                                        if hr - 5 < 0:
                                            print "not enough time left!"
                                        if hr - 5 >= 0:
                                            if hp - x > 0:
                                                mohp = 100
                                            print "You go on a mission"
                                            
                                            print "You encounter a",mo,"!"
                                            
                                            while mohp > 0 or f != 1 or hp > 0:
                                                if hp <= 0:
                                                    print "You died"
                                                    break
                                                if hp > 0:
                                                    if mohp <= 0:
                                                        print "You kill the",mo,"!"
                                                        day = day + 1
                                                        xp = xp + 250
                                                        gold = gold + z
                                                        hr = hr - 5
                                                        print "Your hp is now",hp,"."
                                                        
                                                        print "You got",z,"gold. You have",gold,"gold."
                                                        
                                                        print "You went up",y,"levels. Your level is",ninja,"."
                                                        
                                                        break
                                                    if mohp > 0:
                                                        if f != 1:
                                                            items2 = [0, 1, 1, 1, 2, 3]
                                                            random.shuffle(items2)
                                                            y = items2[2]
                                                            items3 = [5, 10, 15, 11, 13, 17, 7, 21, 25, 27, 30]
                                                            random.shuffle(items3)
                                                            z = items3[2]
                                                            attack1 = raw_input("Do you want to attack using melee (W) or magic (M)? or (I) for inventory items: ")
                                                            
                                                            if attack1 == "W":
                                                                mohp = mohp - weapon * y
                                                                hp = hp - z
                                                                print "You dealt",weapon * y,"damage, using your",ww,". The",mo,"has",mohp,"hp left."
                                                                
                                                                print "You took",z,"damage and now have",hp,"hp."
                                                                
                                                            if attack1 == "M":
                                                                print spell
                                                                sattack = input("what spell do you wish to use?: ")
                                                                if sattack in spell:
                                                                    if mana - sattack * 5 < 0:
                                                                        print "not enough mana"
                                                                    if mana - sattack * 5 >= 0:
                                                                        mohp = mohp - sattack * y * (magic / 5)
                                                                        hp = hp - z
                                                                        mana = mana - sattack
                                                                        print "You used",mw,"and"
                                                                        print "dealt",sattack * y * (magic / 5),"damage! The",mo,"has",mohp,"hp left."
                                                                        
                                                                        print "You took",z,"damage and now have",hp,"hp."
                                                                        
                                                                        print "You have",mana,"mana."
                                                                    if sattack not in q:
                                                                        print "you don't have that spell!"
                                                            if attack1 == "I":
                                                                if EB < 1 or potion < 1:
                                                                    print "You do not have any items"
                                                                if EB >= 1 or potion >= 1:
                                                                    EB_T = raw_input("Do you want to use an Escape Bomb or Potion? E/P/N: ")
                                                                    if EB_T == "E":
                                                                        if EB >= 1:
                                                                            EB = EB - 1
                                                                            print "You sucsessfuly flee."
                                                                            break
                                                                        if EB < 1:
                                                                            print "No escape bombs remaining"
                                                                    if EB_T == "P":
                                                                        if potion >= 1:
                                                                            hp = hp + 100
                                                                        if potion < 1:
                                                                            print "No potions remaining"
                            
                                if ninja < 75:
                                    if hr - 5 < 0:
                                        print "not enogh time left!"
                                    if hr - 5 >= 0:
                                        if hp > 0:
                                            mohp = 100
                                            print "You go on a mission"
                                            
                                            print "You encounter a",mo,"!"
                                            
                                            while mohp > 0 or hp > 0:
                                                if hp <= 0:
                                                    print "You died"
                                                    break
                                                if hp > 0:
                                                    if mohp <= 0:
                                                        print "You kill the",mo,"!"
                                                        day = day + 1
                                                        xp = xp + 150
                                                        gold = gold + z
                                                        hr = hr - 5
                                                        print "Your hp is now",hp,"."
                                                        
                                                        print "You got",z,"gold. You have",gold,"gold."
                                                        
                                                        print "You went up",y,"levels. Your level is",ninja,"."
                                                        
                                                        break
                                                    
                                                    if mohp > 0:
                                                        items2 = [0, 1, 1, 1, 2, 3]
                                                        random.shuffle(items2)
                                                        y = items2[2]
                                                        items3 = [5, 10, 15, 11, 13, 17, 7, 21, 25, 27, 30]
                                                        random.shuffle(items3)
                                                        z = items3[2]
                                                        attack1 = raw_input("Do you want to attack using melee (W) or magic (M). Use an item(I). Or flee: ")
                                                        
                                                        
                                                        if attack1 == "W":
                                                            mohp = mohp - weapon * y
                                                            hp = hp - z
                                                            print "You dealt",weapon * y,"damage, using your",ww,". The",mo,"has",mohp,"hp left."
                                                            
                                                            print "You took",z,"damage and now have",hp,"hp."
                                                            
                                                            
                                                        if attack1 == "M":
                                                            print spell
                                                            sattack = input("what spell do you wish to use?: ")
                                                            if sattack in spell:
                                                                if mana - sattack * 5 < 0:
                                                                    print "not enough mana"
                                                                if mana - sattack * 5 >= 0:
                                                                    mohp = mohp - sattack * y * (magic / 5)
                                                                    hp = hp - z
                                                                    mana = mana - sattack
                                                                    print "You used",mw,"and"
                                                                    print "dealt",sattack * y * (magic / 5),"damage! The",mo,"has",mohp,"hp left."
                                                                    
                                                                    print "You took",z,"damage and now have",hp,"hp."
                                                                    
                                                                    print "You have",mana,"mana."
                                                                if sattack not in q:
                                                                    print "you don't have that spell!"
                                                                    
                                                        if attack1 == "I":
                                                            if EB < 1 or potion < 1:
                                                                print "You do not have any items"
                                                            if EB >= 1 or potion >= 1:
                                                                EB_T = raw_input("Do you want to use an ESCAPE BOMB (E) or HEALTH POTION (P)? E/P/N: ")
                                                                if EB_T == "E":
                                                                    if EB >= 1:
                                                                        EB = EB - 1
                                                                        print "You sucsessfuly flee."
                                                                        break
                                                                    if EB < 1:
                                                                        print "No ESCAPE BOMB(s) remaining"
                                                                if EB_T == "P":
                                                                    if potion >= 1:
                                                                        hp = hp + 100
                                                                    if potion < 1:
                                                                        print "No potions remaining"
                            if work1 == "3":
                                print "Resting..."
                                hp = (ninja * 5) + 100
                                day = day + 1
                                hr = 15
                                mana = pm
                                
                                print "You have",mana,"mana."
                                while CP >= 1 or CP_T != "N":
                                    if CP < 1:
                                        break
                                    if CP >= 1:
                                        if CP_T == "N":
                                            break
                                        CP_T = raw_input("do you want to take a CAFFINE PILL? Y/N: ")
                                        if CP_T == "Y":
                                            CP = CP - 1
                                            hr = hr + 3
                            if work1 == "4":
                                print "You have",gold,"gold"
                                print "Do you wish to buy:"
                                print "-----------------------------"
                                print "1. SHURIKIN (+ 1 Weapon) 10 Gold"
                                print "2. DAGGER (+ 3 Weapon) 20 gold"
                                print "5. DRAGON BLADE (+ 100 Magic & Weapon) 500 Gold"
                                print "6. HEALTH POTION (+100 hp (use later)) 100 gold"
                                print "7. ESCAPE BOMB (1 escape) 25 gold"
                                print "8. CAFFINE PILL (+ 3 hrs) 15 gold"
                                print "9. SPELLS"
                                print "or 0 to leave store"
                                print "---------------------------"
                                shop = raw_input(": ")
                                if hr >= 1:
                                    
                                                
                                        if shop == "6":
                                            if gold < 100:
                                                print "insufficient funds"
                                            elif gold >= 100:
                                                gold = gold - 100
                                                potion = potion + 1
                                                hr = hr - 1
                                                print "you have",potion,"HEALTH POTION(s)."
                                                
                                                print "you now have",gold,"gold"
                                                
                                        elif shop == "7":
                                            if gold < 25:
                                                print "Not enough gold!"
                                            if gold >= 25:
                                                gold = gold - 25
                                                EB = EB + 1
                                                hr = hr - 1
                                                print "You have",EB,"ESCAPE BOMB(s)."
                                                
                                                print "You have",gold,"gold"
                                                
                                        elif shop == "8":
                                            if gold < 15:
                                                print "Not enough gold!"
                                            elif gold >= 15:
                                                CP = CP + 1
                                                gold = gold - 15
                                                hr = hr - 1
                                                print "You have",CP,"CAFFINE PILL(s)."
                                                
                                                print "You have",gold,"gold."
                                                
                                        elif shop == "9":
                                            print "would you like to buy (Type a name for more information):"
                                            print "--------------------------"
                                            for x in range(0, len(PossibleSpell_List)):
                                                print x+1,  PossibleSpell_List[x]
                                            print "or 0 to exit store"
                                            print "--------------------------"
                                            try:
                                                spshop = input(": ")
                                            except Exception:
                                                print "Please just type the number"
                                            if hr >= 1:
                                                print PossibleSpell_List2[spshop-1]
                                                confirm = raw_input("Confirm? Y/N: ")
                                                if confirm == "Y":
                                                    Cost = PossibleSpell_List2[spshop-1]['cost']
                                                    if gold - Cost< 0:
                                                        print "Not enough gold!"
                                                    else:
                                                        Spell_List.append(PossibleSpell_List[spshop-1])
                                                        Spell_List2.append(PossibleSpell_List2[spshop-1])
                                                        gold = gold - Cost
                                                        print "You now have", gold, "gold"
                                                        print "You now have the spells:",
                                                        for x in range(0, len(Spell_List)):
                                                            if x == len(Spell_List)-1:
                                                                print "and " + Spell_List[x] + "."
                                                            else:
                                                                print Spell_List[x] + ",",
                                                    
                                        else:
                                            print "(Remember caps.)"
                                if hr < 1:
                                    print "Not enough time left."

                            elif work1 == "6":
                                E = [spell, weapons, Spell_List, mw, Spell_List2, bw, ww, mana, f, hr, pm, EB, CP_T, CP, gold, weapon, ninja, hp, magic, day, potion, xp]
                                file=open("NinjaAssassinSave.py", 'wb')
                                cPickle.dump(E, file)

                            elif work1=="7":
                                file=open("NinjaAssassinSave.py", 'rb')
                                E = cPickle.load(file)
                                spell = E[0]
                                weapons = E[1]
                                Spell_List=E[2]
                                mw=E[3]
                                Spell_List2=E[4]
                                bw=E[5]
                                ww=E[6]
                                mana=E[7]
                                f=E[8]
                                hr=E[9]
                                pm=E[10]
                                EB=E[11]
                                CP_T=E[12]
                                CP=E[13]
                                gold=E[14]
                                weapon=E[15]
                                ninja=E[16]
                                hp=E[17]
                                magic=E[18]
                                day=E[19]
                                potion=E[20]
                                xp=E[21]
                                

                            elif work1=="8":
                                break
                                
                                

                                    
                            if work1 == "CODES":
                                code = raw_input(": ")
                                if code == "JARVIS":
                                    if hr - 15 < 0:
                                        print "Not enough time"
                                    if hr - 15 >= 0:
                                        ninja = 2500
                                        weapon = 1e+100
                                        magic = 1e+100
                                        mana = 1e+100
                                        pm = 1e+100
                                        hr = hr - 15
                                        gold = 1e+100
                                        potion = 1e+100 
                                        spell.append(50,)
                                        spell.append ("Chidory",)
                                if code == "EHP":
                                    ninja = 75
                                    
                            if work1 == "5":
                                print "gold:",gold,"."
                                print "level:",ninja,"."
                                print "weapon lvl:",weapon,"."
                                print "Melee weapon:",ww,"."
                                print "Magic:",magic,". Mana:",mana,"."
                                print "Spells:",
                                for x in range(0, len(Spell_List)):
                                    if x == len(Spell_List)-1:
                                        print "and " + Spell_List[x] + "."
                                    else:
                                        print Spell_List[x] + ", "
                                print "Collected weapons:",
                                for x in range(0, len(weapons)):
                                    if x == len(weapons)-1:
                                        print "and " +weapons[x] + "."
                                    else:
                                        print weapons[x] + ", "
                                print "hp:",hp,"."
                                print "it is day",day,"."
                                print "Escape Bombs:",EB,"."
                                print "Caffine Pills:",CP,"."
                                print "potions:",potion,"."
                                if bw > 1:
                                    A_C_Weapons = raw_input("Do you wish to Change your melee weapon? Y/N: ")
                                    if A_C_Weapons == "Y":
                                        print weapons
                                        print "Please type in the weapon you want to switch with"
                                        C_Weapons = raw_input(": ")
                                        if C_Weapons in weapons:
                                            ww = C_Weapons
                                            print "Your current melee weapon is now",ww,"."
                                        if C_Weapons not in weapons:
                                            print "You do not have that weapon"

                                if potion > 0:
                                    take = raw_input("do you want to use a potion? (Y) or (N) : ")
                                    if take == "Y":
                                        potion = potion - 1
                                        hp = hp + 100
                                        hr = hr - 1
                                        print "You now have",hp,"hp."
                                        
                                        print "and",potion,"potions"
                                    if potion < 1:
                                        print "not enough potions"
        
        elif option != "H" or option != "N" or option != "Y":
            print "i do not comprehend"
            print ""
