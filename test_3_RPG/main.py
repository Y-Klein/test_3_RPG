from game import Game
if __name__ == "__main__":
    if Game.start() == "s":
        player = Game.create_player(input("enter your name:"))
        monster = Game.choose_random_monster("bob")
        player_roll = Game.roll_dice(6) + player.speed
        monster_roll = Game.roll_dice(6) + monster.speed
        print(f"{player.name} roll + speed = {player_roll}")
        print(f"{monster.type} roll + speed = {monster_roll}")

        if player_roll >= monster_roll:
            validity = player
            attacked = monster
        else:
            validity = monster
            attacked = player
        while player.hp > 0 and monster.hp > 0:
            Game.battle(validity,attacked)
            validity, attacked = attacked, validity
        if player.hp > 0:
            print("🎉🎉🎉")
        else:
            print("😭😭😭")