class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_target(self, target):
        damage = self.attack - target.defense
        if damage > 0:
            target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0