from code.constants import DAMAGE


class GameMediator:
    def __init__(self):
        self.player = None
        self.attacker = None
        self.target = None
        self.enemies = []

    def register_player(self, player):
        self.player = player

    def remove_player(self):
        self.player = None

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

    def check_attack(self, attacker, target):
        self.attacker = attacker
        self.target = target
        if self.attacker.attacking:
            if self.attacker.entity_type != self.target.entity_type:
                if self.attacker.get_attack_rect().colliderect(self.target.get_rect()):
                    self.target.damage(DAMAGE[self.attacker.name])