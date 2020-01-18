from exceptions import EnemyDown
from exceptions import GameOver
import random


class Enemy:
    def __init__(self, level, lives):
        self.lives = lives
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return int(random.choice('123'))

    def decrease_lives(self):
        self.level -= 1
        if self.level == 0:
            raise EnemyDown()
        return self.level


class Player:
    def __init__(self, player_name, lives, score, allowed_attacks):
        self.player_name = player_name
        self.lives = lives
        self.score = score(0)
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        win = [(1, 2), (2, 3), (3, 1)]
        lose = [(1, 3), (2, 1), (3, 2)]
        draw = [(1, 1), (2, 2), (3, 3)]
        fight_case = (int(attack), int(defense))
        if fight_case in win:
            return 1
        if fight_case in lose:
            return -1
        if fight_case in draw:
            return 0
        return 0

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print("Your score is {self.score}\n")
            raise GameOver(self)
        return self.lives

    def attack(self):
        player_choise = int(input("You can choise 1, 2 or 3 to attack: "))
        enemy_attack = Enemy.select_attack()
        if Player.fight(enemy_attack, player_choise) == 0:
            print("It's a draw!")
            self.decrease_lives()
        elif Player.fight(enemy_attack, player_choise) == 1:
            print("You attacked successfully!")
        else:
            print("You missed!")

    def defence(self, enemy_obj):
        player_choise = int(input("You can choise 1, 2 or 3 to defence: "))
        enemy_attack = enemy_obj.select_attack()
        if Player.fight(enemy_attack, player_choise) == 0:
            print("It's a draw!")
            self.decrease_lives()
        elif Player.fight(enemy_attack, player_choise) == 1:
            print("Enemy attacked successfully!")
        else:
            print("Enemy missed!")
