import pygame
from constants import *

class Score:
    def __init__(self, x=0, y=0):
        self.value = 0
        self.position = pygame.Vector2(x, y)
    
    def __repr__(self):
        return f"{self.value}"

    def blit(self, screen):
        font = pygame.font.SysFont('Arial', 30)
        score_display = font.render(f"Score: {self.value}", True, (255, 255, 255))
        pygame.Surface.blit(screen, score_display, (5, 5))

    def add_score(self, added_value):
        self.value += added_value
    
    def get_score(self):
        return self.value
    
