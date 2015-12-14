import os
option=-1
while option !=0:
    option= raw_input ("would you like to play? y/n: ")
    os.system ('cls')
    a=0
    b=0
    while option!="n":
        if option=="n":
            break
        elif option=="y":
            os.system('cls')
            print "*******menu*******"
            print "1. rock"
            print "2. Paper"
            print "3. scisors"
            print "*" *18
            option1= input (" first player, what do you choose? ")
            os.system('cls')
            print "*******menu*******"
            print "1. rock"
            print "2. Paper"
            print "3. scisors"
            print "*" *18
            option2= input (" second player, what do you choose? ")
            os.system ('cls')
            print "rock\n"
            print "paper\n"
            print "saftey scisors\n"
            print "SHOOT!\n"
            print "*******menu*******"
            print "1. rock"
            print "2. Paper"
            print "3. scisors"
            print "*" *18
            option3= ['rock', 'paper', 'scisors' ]
            if option1==1 and option2==2 or option1==2 and option2==3 or option1==3 and option2==1:
                b=b+1
                print "player 2 had", option3[option2-1], "which beats player 1's", option3[option1-1]
            elif option1==option2:
                print "both players had", option3[option1-1], "play again? y/n: "
                option= raw_input()
            else:
                a=a+1
                print "player 1 had", option3[option1-1], "which beats player 2's", option3[option2-1]
            if b==1 and a ==0:
                print "player 2 has won ", b, "out of three matches, one more to go!"
                option= raw_input ("player 2 has 1 point! continue? y/n: ")
            elif b==2:
                option=raw_input ("player 2 won 2 out of 3 matches, player 2 wins the game! play again? y/n: ")
            if a==1 and b==0:
                print "player 1 has won ", a, "out of three matches, one more to go"
                option= raw_input ("player 1 has 1 point! continue? y/n: ")
            if a==1 and b==1:
                option=raw_input ("both players have 1 win, next round wins! pla again? y/n: ")
            elif  a==2:
                option=raw_input ("player 1 won 2 out of 3 matches, player 2 wins the game! play again? y/n: ")
            if b==2 or a==2:
                a=0
                b=0


