import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    a_field = AsteroidField()

    #initiate player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)
    
    #feels cursed to do this, but fine.
    while True:
        #logging state
        log_state()
        
        #glad we have this now
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updatable.update(dt)
        
        #checking each asteroid collision with each shot
        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    new_ast = a.split()

                    #checking if it split successfully
                    if len(new_ast) > 0:
                        asteroids.add(new_ast[0])
                        asteroids.add(new_ast[1])
                    s.kill()

            if a.collides_with(player):
                log_event("player_hit")
                sys.exit()

        for drw in drawable:
            drw.draw(screen)

        #refresh screen
        pygame.display.flip()
        dt = clock.tick(60)/1000
        #print(dt)
        

if __name__ == "__main__":
    main()
