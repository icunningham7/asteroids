# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from score import Score
from level import Level
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    blitable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    hud = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable, blitable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for drawn in drawable:
            if drawn.position[0] + drawn.radius < 0:
                drawn.position = pygame.Vector2(SCREEN_WIDTH, drawn.position[1])
            if drawn.position[0] - drawn.radius > SCREEN_WIDTH:
                drawn.position = pygame.Vector2(0, drawn.position[1])
            if drawn.position[1] + drawn.radius < 0:
                drawn.position = pygame.Vector2(drawn.position[0], SCREEN_HEIGHT)
            if drawn.position[1] - drawn.radius > SCREEN_HEIGHT:
                drawn.position = pygame.Vector2(drawn.position[0], 0)

        for asteroid in asteroids:
            if (asteroid.collides_with(player)):
                player.take_damage()
                asteroid.kill()
            for shot in shots:
                if asteroid.collides_with(shot):
                    score = asteroid.split()
                    player.add_score(score)
                    shot.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        player.score.blit(screen)
        player.level.blit(screen)
        player.lives.blit(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
