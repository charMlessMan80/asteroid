# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to help control the frame rate
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update the screen
        player.update(dt)

        # Draw the screen
        screen.fill((0, 0, 0))
        player.draw(screen)
        
        pygame.display.flip()

        # Limit the frame rate to 60 fps
        clock.tick(60)
        dt = clock.get_time()/1000

if __name__ == "__main__":
    main()
