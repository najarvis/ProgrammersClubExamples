import random
names=["Billy", "Bob", "Joe", "Giles", "Jill", "Nick", "goku", "dovah khin", "mike", "Ike"]
class player(object):

      def __init__(self):
           pass

class citizen(player):

      def __init__(self, name):
           citizen.name=name


name = names[0]
citizen=citizen(name)
option=raw_input("play? y/n: ")
while option=="y":
      citizen=citizen(name)
      names=["Billy", "Bob", "Joe", "Giles", "Jill", "Nick", "goku", "dovah khin", "mike", "Ike"]
      random.shuffle(names)
      print "%s" %(citizen.name)    
      option=raw_input("again? y/n: ")
