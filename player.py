import sys
import pygame
from circleshape import CircleShape
from shot import Shot
from score import Score
from lives import Lives
from level import Level
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        self.shot_speed_modifier = 1
        self.invulnerable_timer = 0
        self.score = Score()
        self.lives = Lives()
        self.level = Level()


        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        self.shoot_timer -= dt
        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= dt
        self.position += self.velocity
        keys = pygame.key.get_pressed()


        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.accelerate(dt)
        if keys[pygame.K_s]:
            self.accelerate(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        self.velocity += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1 ).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN * self.shot_speed_modifier

    def add_score(self, added_value):
        self.score.add_score(added_value)
        self.add_xp(added_value)
        print(f"Current Score: {self.score}")
    
    def add_xp(self, added_xp):
        starting_level = self.level.get_level()
        level_up = self.level.add_xp(added_xp)
        if level_up > 0:
            self.shot_speed_modifier = (1 - (0.05 * self.level.get_level())) if (1 - (0.05 * self.level.get_level())) > 0 else 0.05
            for levels in range(starting_level + 1, (starting_level + level_up + 1)):
                if levels % 5 == 0:
                    self.lives.add_lives(1)


    def lose_life(self):
        self.lives.lose_life()
        
        self.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.velocity = pygame.Vector2(0,0)
        self.rotation = 0
        self.invulnerable_timer = PLAYER_INVULNERABLE_COOLDOWN
        print(f"Lives Remaining: {self.lives}")
    
    def take_damage(self):
        if self.invulnerable_timer <= 0:
            self.lose_life()

class Player_Experience:
    def __init__(self, x=0, y=0):
        self.current_ex
        self.needed_ex
        self.position = pygame.Vector2(x, y)
    
    def __repr__(self):
        return f"{self.value}"

    def blit(self, screen):
        font = pygame.font.SysFont('Arial', 30)
        score_display = font.render(f"Level: {self.level} Experience: {self.value}", True, (255, 255, 255))
        pygame.Surface.blit(screen, score_display, (5, 70))

    def add_score(self, added_value):
        self.value += added_value
    
    def get_score(self):
        return self.value