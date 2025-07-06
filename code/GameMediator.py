class GameMediator:
    def __init__(self):
        self.player = None
        self.enemies = []

    def register_player(self, player):
        self.player = player

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def destroy_enemy(self, enemy):
        self.enemies.remove(enemy)

    def count_enemies(self):
        return len(self.enemies)

    def get_player_position(self):
        if self.player:
            return self.player.position
        return None