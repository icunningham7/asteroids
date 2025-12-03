import pygame

class Level:
    def __init__(self, starting_level=1, starting_xp=0, x=0, y=0):
        self.value = starting_level
        self.xp = starting_xp
        self.xp_threshold = 100
    
    def __repr__(self):
        return f"Level: {self.value}"

    def blit(self, screen):
        font = pygame.font.SysFont('Arial', 30)
        level_display = font.render(f"Level: {self.value}", True, (255, 255, 255))
        pygame.Surface.blit(screen, level_display, (5,5))

    def level_up(self):
        self.value += 1
        self.xp_threshold *= 2 - (0.05 * self.value)
        return True

    def add_xp(self, xp):
        self.xp += xp
        level_ups = 0
        while self.xp >= self.xp_threshold:
            self.xp - self.xp_threshold
            self.level_up()
            level_ups += 1
        return level_ups

    def get_level(self):
        return self.value
    
    def get_xp(self):
        return self.xp