import random

class Player:
    def __init__(self,name):
       self.name = name
       self.hp = 50
       self.speed = random.randint(5, 10)
       self.power = random.randint(5, 10)
       self.armor_rating = random.randint(5, 15)
       self.profession = random.choice(["cure", "fighter"])

    def is_cure(self):
        self.hp += 10

    def is_fighter(self):
        self.power += 2

    def speak(self):
        print(f"my name is {self.name}")

    def attack(self):
        pass

