from exceptions import EnemyDown
from exceptions import GameOver
from models import Enemy
from models import Player


def play():
    player_name = (input("Enter your name: ")
    player = Player(player_name)
    level = 1
    enemy = Enemy(1)

    print('Hello', player_name, "please enter command 'START' to start the game.")
    start = str(input())
    Player(start)
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
        return 0
