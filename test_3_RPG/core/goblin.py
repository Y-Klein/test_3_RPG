import random


class Goblin:
    def __init__(self,name):
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.armor_rating = 1
        self.weapon = random.choice(["Knife", "sword", "axe"])

    def speak(self):
        print(f"the goblin {self.name} is angry")

    def attack(self):
        pass
