import sys 
import pygame
from constants import *

class Lives:
    def __init__(self, x=0, y=0):
        self.value = 3
        self.position = pygame.Vector2(x, y)
    
    def __repr__(self):
        return f"{self.value}"

    def blit(self, screen):
        font = pygame.font.SysFont('Arial', 30)
        lives_display = font.render(f"Lives: {self.value}", True, (255, 255, 255))
        pygame.Surface.blit(screen, lives_display, (5, 35))

    def add_lives(self, lives_to_add):
        self.value += lives_to_add
        if self.value < 0:
            sys.exit()
        return self.value
    
    def lose_life(self):
        return self.add_lives(-1)
    
    def get_lives(self):
        return self.value
    
