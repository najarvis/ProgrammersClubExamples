import Character
import Enemies

def main():
    main_player = Character.Character("Jarvis")
    main_player.get_standard_character()
    main_player.print_attributes()

    first_enemy = Enemies.Goblin()
    first_enemy.print_attributes()

    second_enemy = Enemies.Goblin("Goblin 2")
    second_enemy.print_attributes()

    enemies = [first_enemy, second_enemy]

    while len(enemies) > 0 and main_player.health > 0:
        dead_enemies = []
        for en in enemies:
            en.print_short()
        choice = raw_input("Who do you want to attack?")
        main_player.attack(first_enemy)

if __name__ == "__main__":
    main()
