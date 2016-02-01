"""This is our first program that uses pygame. It's really not that bad!

This code is the base of almost every program,
so it is important to understand it.
"""

import pygame

def draw_primitives(surface, screen_size):
    """We will draw the primitives in this function, in order
    to keep our code neat and clean."""

    width, height = screen_size
    pygame.draw.rect(surface, (255, 255, 255), (20, 20, 100, 50))
    pygame.draw.rect(surface, (0, 0, 255), (width * 0.75, 50, 50, 50), 3)
    pygame.draw.circle(surface, (255, 0, 0), (width / 2, height / 2), 20)

    points = [(0, height), (width / 2, height / 2), (width, height)]
    pygame.draw.polygon(surface, (0, 255, 0), points)


def main():
    """The main function of the program.

    creates the main screen, handles the main loop,
    gets and handles input, and updates the screen
    """

    screen_size = (640, 480) # Create a variable to store the size of the screen
    screen = pygame.display.set_mode(screen_size) # Initialize the screen
    pygame.display.set_caption("PyGame is Working!") # Set window caption

    done = False # Create a variable control the main loop, "are we done?"
    while not done: # Main loop
        for event in pygame.event.get(): # get all of the events
            if event.type == pygame.QUIT: # X on the window is clicked
                done = True
            elif event.type == pygame.KEYDOWN: # Any button is pressed
                if event.key == pygame.K_ESCAPE: # Hit the Escape button
                    done = True

        screen.fill((0, 0, 0)) # Fill the screen with black every frame
        draw_primitives(screen, screen_size)

        pygame.display.update() # Update the screen (DON'T FORGET THIS)

if __name__ == "__main__": # The code inside here will only
    main()                 # execute if this file is ran directly

