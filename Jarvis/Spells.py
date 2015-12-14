#WEAK--------------------------------------------------------------------------

Weak_Fireball = {'name': 'Weak Fireball', 'power' : 5, 'mana': 10, 'skill_level': 1}

Weak_Iceball = {'name': 'Weak Iceball', 'power': 7, 'mana': 15, 'skill_level': 3}

Weak_Bolt = {'name': 'Weak Bolt', 'power': 10, 'mana': 21, 'skill_level': 6}

Weak_Leech = {'name': 'Weak Leech', 'power': 5, 'mana': 25, 'skill_level': 6, 'heal': 5}

Weak_Heal = {'name': 'Weak Heal', 'power': 0, 'mana': 15, 'skill_level': 5, 'heal': 15}

Weak_Spells = [Weak_Fireball, Weak_Iceball, Weak_Bolt, Weak_Leech, Weak_Heal]

#NORMAL------------------------------------------------------------------------

Fireball = {'name': 'Fireball', 'power': 20, 'mana': 45, 'skill_level': 12}

Iceball = {'name': 'Iceball', 'power': 25, 'mana': 55, 'skill_level': 15}

Bolt = {'name': 'Bolt', 'power': 32, 'mana': 70, 'skill_level': 18}

Leech = {'name': 'Leech', 'power': 20, 'mana': 75, 'skill_level': 20, 'heal': 20}

Heal = {'name': 'heal', 'power': 0, 'mana': 65, 'skill_level': 15, 'heal': 50}

Normal_Spells = [Fireball, Iceball, Bolt, Leech, Heal]

#STRONG------------------------------------------------------------------------

Strong_Fireball = {'name': 'Strong Fireball', 'power': 50, 'mana': 110, 'skill_level': 25}

Strong_Iceball = {'name': 'Strong Iceball', 'power': 60, 'mana': 130, 'skill_level': 30}

Strong_Bolt = {'name': 'Strong Bolt', 'power': 75, 'mana': 150, 'skill_level': 42}

Strong_Leech = {'name': 'Strong Leech', 'power': 50, 'mana': 160, 'skill_level': 50, 'heal': 50}

Strong_Heal = {'name': 'Stong Heal', 'power': 0, 'mana': 150, 'skill_level': 45, 'heal': 110}

Strong_Spells = [Strong_Fireball, Strong_Iceball, Strong_Bolt, Strong_Leech, Strong_Heal]

#HOLY------------------------------------------------------------------------

Holy_Lightning = {'name': 'Holy Lightning', 'power': 500, 'mana': 1000, 'skill_level': 100}

Holy_Spells = [Holy_Lightning]

All_Spells = [Weak_Spells, Normal_Spells, Strong_Spells, Holy_Spells]
