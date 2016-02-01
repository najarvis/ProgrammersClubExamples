"""This is our first program that uses pygame. It's really not that bad!

This code is the base of almost every program,
so it is important to understand it.
"""

import pygame

def main():
    """The main function of the program.

    creates the main screen, handles the main loop,
    gets and handles input, and updates the screen
    """

    screen_size = (640, 480) # Create a variable to store the size of the screen
    screen = pygame.display.set_mode(screen_size) # Initialize the screen
    pygame.display.set_caption("PyGame is Working!") # Set window caption

    surface1 = pygame.Surface((64, 64))
    surface1.fill((255, 255, 0))

    done = False # Create a variable control the main loop, "are we done?"
    while not done: # Main loop
        for event in pygame.event.get(): # get all of the events
            if event.type == pygame.QUIT: # X on the window is clicked
                done = True
            elif event.type == pygame.KEYDOWN: # Any button is pressed
                if event.key == pygame.K_ESCAPE: # Hit the Escape button
                    done = True

        screen.fill((0, 0, 0)) # Fill the screen with black every frame
        screen.blit(surface1, (100, 100))
        pygame.display.update() # Update the screen (DON'T FORGET THIS)

if __name__ == "__main__": # The code inside here will only
    main()                 # execute if this file is ran directly

