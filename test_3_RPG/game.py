import random
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin

class Game:
    @staticmethod
    def start():
        return input(Game.show_menu())
    @staticmethod
    def show_menu():
        return "menu:\nPress's'to start game\nPress any key to exit. "

    @staticmethod
    def create_player(name)-> Player:
        show_player= Player(name)
        return show_player

    @staticmethod
    def choose_random_monster(name)-> Goblin|Orc:
        if random.getrandbits(1):
            x = Orc(name)
        else:
            x = Goblin(name)
        return x

    @staticmethod
    def battle(validity, attacked):
        print(f"{validity.name} is validity")
        x = Game.roll_dice(20) + validity.speed
        if x > attacked.armor_rating:
            print("injury")
            Game.damage_inspection(validity,attacked)
            print(f"{attacked.name} hp is: {attacked.hp}")
        else:
            print("miss")


    @staticmethod
    def damage_inspection(validity, attacked):
        damage = Game.roll_dice(6) + validity.power
        try:
            if validity.weapon == "Knife":
                damage *= 0.5
            elif validity.weapon == "axe":
                damage *= 1.5
        except:
            pass
        attacked.hp -= damage

    @staticmethod
    def roll_dice(sides:int)-> int:
        return random.randint(1,sides)
