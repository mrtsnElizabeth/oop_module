from exceptions import GameOver
from models import Player


if name == '__main__':
    result = None
    try:
        play()
    except exceptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye')

def play():
    player_name = print(str(input("Enter your name: ")))
    player = Player(player_name)
    enemy = Enemy(level=1)
    print('Hello', player_name, "please enter command 'START' to start the game")
    command_start = str(input())
    Player(command_start)
    if command_start == "START":
        player.attack(enemy)
