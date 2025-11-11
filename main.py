import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    #initiate player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
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
        
        for drw in drawable:
            drw.draw(screen)

        #refresh screen
        pygame.display.flip()
        dt = clock.tick(60)/1000
        #print(dt)
        

if __name__ == "__main__":
    main()
