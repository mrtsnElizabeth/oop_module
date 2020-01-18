class GameOver(Exception):
    def __init__(self, some_obj):
        super().__init__()
        self.player_name = str(some_obj.player_name)
        self.player_score = str(some_obj.player_score)


class EnemyDown(Exception):
    pass
