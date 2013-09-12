#This is a library for inputing text through a GUI from the. I only slightly changed it to suit our purposes. 
# Run take_input, returns whatever user inputs

# EzText example
from pygame.locals import *
import pygame, sys, eztext

def take_input():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((640,240))
    # fill the screen w/ white
    screen.fill((255,255,255))
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here: '
    txtbx = eztext.Input(maxlength=4, color=(255,0,0), prompt='Amount of food:  ')
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    while 1:
        # make sure the program is running at 30 fps
        clock.tick(30)

        # events for txtbx
        events = pygame.event.get()
        # process other events
        for event in events:
            # close it x button si pressed
            if event.type == QUIT: 
                return txtbx.value

        # clear the screen
        screen.fill((255,255,255))
        # update txtbx
        txtbx.update(events)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()

