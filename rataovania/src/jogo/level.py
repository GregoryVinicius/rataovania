class Level:
    def __init__(self, background, player):
        self.background = background
        self.player = player
        self.enemies = []

    def load(self):
        # Load level assets and initialize enemies
        pass

    def update(self):
        # Update player and enemies
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        # Draw the background, player, and enemies
        screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)