import time
import os
def courtyard():
     print"you see that the fountain in the courtyard isnt working"
     print"you see a switch on the ground"
     option1=raw_input(">>>")
commands= "******************************\ncommands:\nn= north\ne= east\ns= south\nw= west\ninvestigate\ncommand=print command list\nmay be more commands are hidden\n*****************************"
option="a"
option1="a"
option2="a"
option3="a"
option4="a"
option5="a"
print "************CHIMMNEY CASTLE************"
time.sleep(1.5)
print "a text based adventure game!"
time.sleep(1)
o=raw_input("do want to play y/n: ")
print "*" *40, "\n"
if o=="y":
     print "*" *29
     print "USE NO CAPS!!!"
     print "commands: "
     time.sleep(.5)
     print "n= north"
     time.sleep(.5)
     print "e= east"
     time.sleep(.5)
     print "s= south"
     time.sleep(.5)
     print "w= west"
     time.sleep(.5)
     print "investigate"
     time.sleep(.5)
     print "command= command list"
     time.sleep(.5)
     print "may be more commands, hidden"
     time.sleep(.5)
     print "*" *29, "\n\n\n"
     time.sleep(1.5)
     print "you are on the outside of the chimmney castle"
     print "there is a courtyard to your west and a hedge"
     print "maze to your east, the house looks like it"
     print "has no entry"
     option=raw_input(">>>")
     if o!="y":
          print "goodbye"
          time.sleep(1.5)
          quit
     if option=="w":
          courtyard()
          if option1=="investigate":
               print "the fountain makes a interesting sound and it does not work"
               option2=raw_input(">>>")
     if option=="command":
          print commands
          option1=raw_input(">>>")
     else:
          print "that is not a valid option"
          option1=raw_input(">>>")
