from exceptions import EnemyDown
from exceptions import GameOver
from models import Enemy
from models import Player


def play():
    player_name = (input("Enter your name: ")
    player = Player(player_name)
    level = 1
    enemy = Enemy(1)

    print(str("Choose your Player: 1 - MAG, 2 - WARRIOR, 3 - ROGUE"))
              pl_char = int(input())
              if pl_char == 1:
                  print('Your Choose MAG. Good luck!')
                  enemy_obj.decrease_lives()
              elif pl_char == 2:
                  print("Your Choose WARRIOR. Good luck!")
              elif pl_char == 3:
                  print("Your Choose ROGUE. Good luck!")

    print('Hello', player_name, "please enter command 'START' to start the game.")
    start = str(input())
    player = Player(start)
    if start == "START":
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            level += 1
        player.score += 5
        enemy = Enemy(level)


if __name__ == '__main__':
    try:
        play()
    except GameOver as gover:
        print("GameOver")
        sc_file = open('scores.txt', 'a')
        sc_file.write(gover.player_name + gover.player_score + '\n')
        sc_file.close()
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye')

