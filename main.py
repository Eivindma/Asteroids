import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    astroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    AsteroidField.containers = updatable
    Asteroid.containers = (updatable, drawable, astroids)
    asteroid_field = AsteroidField()
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)
            
        for astroid in astroids:
            if player.check_collision(astroid):
                print("Game over!")
                sys.exit()
                
        for shot in shots:
            for astroid in astroids:
                if shot.check_collision(astroid):
                    shot.kill()
                    astroid.split()
                     
                  
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        
        
        pygame.display.flip()
        dt =  clock.tick(60) / 1000
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()