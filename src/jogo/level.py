class Level:
    def __init__(self, background, player):
        self.background = background
        self.player = player
        self.enemies = []

    def load(self):
        pass

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)