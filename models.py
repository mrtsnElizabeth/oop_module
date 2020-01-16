import random


class Enemy:

    def __init__(self, level, lives):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        pass

    def decrease_lives(self):
        self.level -= 1
        if self.level == 0:
            raise EnemyDown()
        return self.level

class Player:

    def __init__(self, name, lives, score, allowed_attacks):
        pass

    @staticmethod
    def fight(attack, defense):
        pass

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver()
        return self.lives

    def attack(self, enemy_obj):
        if command_start == "START":
            print(str("Choose your HERO: 1 - MAG, 2 - WARRIOR, 3 - ROGUE"))
            hero = int(input())
            if hero == 1:
                print('Your Choose MAG, Goog luck!')
            elif hero == 2:
                print("YEAH, It's WARRIOR!!")
            elif hero == 3:
                print("FUCK, You are ROGUE, be careful")

    def defence(self, enemy_obj):
        self.enemy_obj = enemy_obj
