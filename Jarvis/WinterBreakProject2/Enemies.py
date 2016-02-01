import Character
import Weapons


class Goblin(Character.Character):

    def __init__(self, name="Goblin"):
        Character.Character.__init__(self, name)
        self.get_standard_character('2d5')

        self.inventory = {"Short Sword": Weapons.ShortSword()}

        self.current_weapon = "Short Sword"
