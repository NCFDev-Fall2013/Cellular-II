import pygame, threading
from pygame.locals import *

#GUI.py holds all GUI elements fabricated from pygame for use with pygame
#the elements are as follows:
#gameWindow (isA Surface)- the entire window, the base display 
    #has frames
    #has size
    #has closing behavior
    #has opening behavior

#window_thread = threading.Thread
Thread = threading.Thread

class gameWindow(pygame.Surface,Thread):
    def __init__(self, initialFrameList, size, closeBehavior, openBehavior, title):
        super(gameWindow,self).__init__(size)
        Thread.__init__(self)
        self.window_size = size #tuple with width and height
        self.all_frames = initialFrameList #start everything contained in the window
        self.unadded_frames = initialFrameList
        self.on_close = closeBehavior #should usually be quit on close
        self.on_open = openBehavior #might initialize a startscreen or whatever
        self.window_title = title
        self.is_open = False
        
    def window_start(self):
        pygame.init()
        showMe = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)
        self.fill((250,250,250))
        pygame.display.update()
        self.is_open = True
        self.start()
        self.run()

    def run(self):
        print self.is_open,
        while self.is_open:
            #print 'about to update...'
            self.update_frames()   
            for event in pygame.event.get():
                #if event.type == HCADD:
                 
                if event.type == QUIT:
                    pygame.quit()
                    self.is_open = False
                    return()

    def add_frame(self,frame):
        print 'adding ', frame
        self.unadded_frames.append(frame)
        #add_event = pygame.event.Event(HCADD)
        #pygame.event.pos(add_event)

    def update_frames(self):
        for f in self.all_frames:
            if f in self.unadded_frames:
                self.blit(f,f.position)
                print 'adding'
                if f in self.unadded_frames:
                    self.unadded_frames.remove(f)
            pygame.display.update()
        
            
#gameFrame (isA Surface)- a section of a game window - essentially a subsurface
    #has inputs
    #has outputs
    #has size
    #has (absolute) coordinates
    #has background color
    #has own coordinate system

class gameFrame(pygame.Surface):
    def __init__(self,elements,size,pos,bcolor):
        super(gameFrame,self).__init__(size)
        self.all_elements = elements
        self.frame_size = size
        self.position = pos
        self.background_color = bcolor
        self.fill(self.background_color)
        self.coordinate_system = []

    def show(self):
        showMe = pygame.display.set_mode(self.frame_size)
        pygame.display.update()

        
        
#screens (isA Surface)- interactive, but to a limited extent - screens are simply specific types of frames
#gameScreen (isA gameFrame) - superClass facilitating screen polymorphism
    #has background image
    #has animation
    #has textBox(es)
    #has music
    #has Layout

#gameStartScreen (isA gameScreen) - functioning subclass
    #has action
    #has prompt text
    #has display text

#gameMenuScreen (isA gameScreen) - functioning subclass
    #has menu(s)

#gameLoadScreen (isA gameScreen) - functioning subclass
    #has display text
    #has loader

#gamePlayerScreen (isA gameScreen) - functioning subclass
    #this is the least defined screen - the layout is nixed
    #this is meant to be the playable screen

#gameDebugScreen (isA gameScreen) - functioning subclass
    #prints debugging statements 
    
#menus - navigable, clickable beasts
#gameMenu (isA gameFrame) - basically a collection of buttons which have a layour
    #has buttons
    #has Menulayout
    #has collapseability

#HUDs (isA gameFrame) - more flexible visually than menus (treated more as an element than a frame...)
    #has opacity
    #has parent frame
    #has HUDlayout

#gameInout (isA Surface)- a superClass facilitating polymorphism for GUI inputs and outputs
    #has listening capability
    #has a frame
    #has (relative) coordinates
    #is stackable
    #has size
    #has color

#text boxes
#gameTextBox (isA gameInOut) - a superClass facilitating polymorphism for textBoxes
    #has font
    #has fontColor
    #has fontSize
    #has background
    #has a text argument
    #capable of displaying its text argument
    #has a source
#gameTextIn (isA gameTextBox) - a functioning subclass which allows user input for text
    #capable of taking user input
#gameTextOut (isA gameTextBox) - a functioning subclass which displays some output
    #might not actuallty be a class

#buttons
#gameButton (isA gameInOut) - a superclass facilitating polymorphism for buttons
    #has notPressedImage
    #has pressedImage
    #has display text
    #has sleepTime
    #has action
    #has message

#TOOLS

#coordinateSystem - facilitates coordinates for gameFrames (makes element placement easier)
    #can access elements at given coordinate
    #has a list of contained elements
    #has gridding capability
    #has gridding scale
    #has origin coordinates
    #constructs self around origin

#3dcoordinateSystem (not quite a coordinateSystem) - facilitates 3d capablities
    #constructs 3d phantom system around origin
    #might not be pursued

#gameLayout -
    #has frameRegions
    #constrains passed gameFrames to regions
    #has elementRegions
    #constrains passed elements to regions
    #has a coordinateSystem
#frameLayout (isA gameLayout) -
    #has a parent frame
#windowLayout (isA gameLayout) -
    #has a parent window

#trigger - basically just a message sent between things in pygame

#Animation (isA Thread)- facilitates animation in pygame (this is superclass)
    #has interval
    #has triggersIn
    #has triggersOut
    #has transformList

#SpriteAnimation (isA Animation)
    #has a spriteArray
    #implements transformList (runs)

#ImageAnimation (isA Animation)
    #has an image
    #implements transformList (runs)

#RectAnimation (isA Animation)
    #has a rect
    #implements transformList (runs)

#Transformer - facilitates the ridiculous transformation stuff that happens
    #can transform GUI elements
    #can transform Images
    #can transform Sprites
    #can transform Rects
    #CANNOT TRANSFORM GAMEFRAMES
