def print_spells():
    import Spells
    w = 0
    for x in range(0, len(Spells.All_Spells)):
        for y in range(0, len(Spells.All_Spells[x])):
            w = w + 1
            print w, Spells.All_Spells[x][y]['name']

def define_spells(a):
    import Spells
    w = 0
    for x in range(0, len(Spells.All_Spells)):
        for y in range(0, len(Spells.All_Spells[x])):
            w = w + 1
            a.append(Spells.All_Spells[x][y]['name'])

def list_spells(a):
    import Spells
    w = 0
    for x in range(0, len(Spells.All_Spells)):
        for y in range(0, len(Spells.All_Spells[x])):
            w = w + 1
            a.append(Spells.All_Spells[x][y])
