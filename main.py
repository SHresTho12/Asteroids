# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0
    
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable =pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = ( updatable , drawable , shots)
    
    
    player = Player(x,y)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        for ast in asteroids:
            if player.is_colliding(ast):
                print("Game over!")
                sys.exit(0)
        
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clk.tick(60) / 1000

if __name__ == "__main__":
    main()