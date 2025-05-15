import pygame
from constant import GROUND_LEVEL
from jogo.entity import Entity

class Character(Entity, pygame.sprite.Sprite):
    def __init__(self, name, health, damage, defense, velocity, resultant_force=None, y_velocity=0, on_ground=False, x=0, y=0, width=50, height=50):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.velocity = velocity
        self.resultant_force = resultant_force  # Intensidade da gravidade
        self.y_velocity = y_velocity  # Velocidade vertical inicial
        self.on_ground = on_ground  # Verifica se o personagem está no chão
        self.ground_level = GROUND_LEVEL  # Nível do chão (pode ser ajustado conforme necessário)

        # Cria um retângulo para o personagem (necessário para colisão e movimentação)
        self.rect = pygame.Rect(x, y, width, height)
        # Opcional: criar uma imagem para desenhar o personagem
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))  # Verde, por exemplo

    def attack(self, target):
        damage = self.damage - target.defense
        if damage > 0:
            target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def apply_gravity(self, gravity=None, time=1):
        if gravity is None:
            gravity = self.resultant_force or 0
    
        max_fall_speed = 15
    
        if not self.on_ground:
            self.y_velocity += gravity * time  # Incrementa a velocidade vertical
            if self.y_velocity > max_fall_speed:
                self.y_velocity = max_fall_speed
            self.rect.y += self.y_velocity  # Atualiza a posição com a velocidade
    
            if self.rect.y >= self.ground_level:
                self.rect.y = self.ground_level
                self.y_velocity = 0
                self.on_ground = True
        else:
            self.y_velocity = 0
            
        