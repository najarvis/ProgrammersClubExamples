import random
from pprint import pprint

def new_deck(shuffle=False, Seed=False, Long=False):
    if Seed and shuffle:
        random.seed(Seed)
    clist = []

    if Long:
        unique_cards = ['Ten', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        x=' of '
        for i in suits:
            for b in range(2, 10):
                clist.append((str(b)+x+i))
                
            for a in unique_cards:
                clist.append((a+x+i))
                
    else:
        unique_cards = ['T', 'J', 'Q', 'K', 'A']
        suits = ['h', 'd', 'c', 's']

    
        for i in suits:
            for b in range(2, 10):
                clist.append((i+str(b)))
                
            for a in unique_cards:
                clist.append((i+a))

    if shuffle:
        random.shuffle(clist)
    return clist

def draw_cards(num, deck=new_deck()):    #number of cards drawn
    player_cards = []
    for i in range(num):
        player_cards.append(deck.pop(0))

    player_cards.sort()

    return player_cards

def get_suits(lst=new_deck()):
    hearts = []
    diamonds = []
    spades = []
    clubs = []
    for i in range(len(lst)):
        if lst[i][0] == "s":
            spades.append(lst[i])
        elif lst[i][0] == "h":
            hearts.append(lst[i])
        elif lst[i][0] == "c":
            clubs.append(lst[i])
        elif lst[i][0] == "d":
            diamonds.append(lst[i])

    suits = {'Hearts':hearts, 'Diamonds':diamonds, 'Spades':spades, 'Clubs':clubs}
    for i in suits:
        pprint((i, suits[i]), indent=4)

if __name__ == "__main__":
    new_deck()
