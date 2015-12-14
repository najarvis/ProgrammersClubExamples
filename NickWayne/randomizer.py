import random
option="y"
option2="glue"
option2= raw_input (" enter password: ")
if option=="y":
    print "*******menu*******"
    print "1. randomizer"
    print "2. lucky number genorator"
    
    a=0
    while True:
        x= random.randint(1, 2000)
        print x
        a=a+1
    	if x==1234:
            print "it took", a, "lines to get 1234 on the randomizer"
            option=raw_input("play again? y/n: ")
            a=0
            

