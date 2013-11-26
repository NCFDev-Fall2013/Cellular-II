
#====Built-in Modules====#
import sys, threading, random

#====Required Modules====#
from pygame.locals import *
import pygame, pygame.gfxdraw

# These are the variables everyone's talking about
cell_record = {}
origin_cells = []

# Gets things started
Thread = threading.Thread
pygame.init()
display_width = 250
display_width = 750
window_object = pygame.display.set_mode((display_width, display_height))

class Window(Thread):
        def run(self):
                while True:
                        # Clean slate!
                        window_object.fill((255,255,255))
