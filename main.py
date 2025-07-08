# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create a window from width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Look at this! a Clock for our game
    clock = pygame.time.Clock()
    
    #make some groups before the variables
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #just like groups we need the container values above the variables they use
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)

    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()


    Player.containers = (updateable, drawable)
    

    #make a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    
    #the speed delta
    dt = 0
        
    # The magic goes here
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        
        #lets make sure we draw all the stuff in the drawable container
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # Making sure our frames don't go past 60 per loop. Thanks clock!
        dt = clock.tick(60) / 1000
        
        

    
if __name__ == "__main__":
    main()

   