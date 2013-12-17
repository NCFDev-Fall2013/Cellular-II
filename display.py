#====Built-in Modules====#
import sys, threading, random, math

#====Required Modules====#
from pygame.locals import *
import pygame, pygame.gfxdraw

#=====Custom Modules=====#
#from environment import World
import environment
World = environment.World
from virus import Virus

# Create a position class so we can add food via a mouse click
# i guess i should import vector or something, but I did this instead
class Position():
        def __init__(self, loc_tuple):
                self.x = loc_tuple[0]
                self.y = loc_tuple[1]

#set color constants
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)

#images
play_pause_img = pygame.image.load('play_pause.bmp')
add_viruses_img = pygame.image.load('add_viruses.bmp')
add_cells_img = pygame.image.load('add_cells.bmp')
add_food_img = pygame.image.load('add_food.bmp')
reset_img = pygame.image.load('reset.bmp')

# i'm pretty sure we don't need this
#mousex, mousey = 0,0

# start a thread so that we can later prevent World from changing the list of cells while we interate through it
Thread = threading.Thread

# starts pygame
pygame.init()

# i don't think we need this
#fpsClock = pygame.time.Clock()

# set dimensions of display window
world_width = 500
world_height = 500
display_width = int(1.5*world_width)
display_height = world_height
windowSurfaceObj = pygame.display.set_mode((display_width,display_height))

#window title
pygame.display.set_caption('Nautical Cell Force 2')

#button class
# the button name is also the name of the function it when clicked
class Button():
    button_xlocs = .36*world_width*3
    button_radiuses = .05*display_height

    def __init__(self,name,height,img):
        self.name =name
        self.xloc = Button.button_xlocs
        self.yloc = height
        self.image = img
        self.radius = Button.button_radiuses

        # button functions
    def play_pause(self):
        if Display.running_bool == True: Display.running_bool = False
        else: Display.running_bool = True
	print "pause"
    def add_viruses(self):
        environment.add_viruses(1)
	print "submit to the viruses!"
    def add_cells(self):
        environment.add_cells(1)
	print "add cell"
            
    def reset(self):
        dupe = World.cell_list[:]
        for cell in dupe:
                World.remove_cell(cell)
	print "reset"
    def add_food(self):
        environment.add_food(1)
	print "add food"
    def click(self):
	    print "clicking", "self."+self.name+"()"
	    print self.name
	    eval('self.'+self.name+'()')
	    #        eval(self.name+'()')
	    #      eval(function)
#button_locations
#play-pause,settings, cell designer, state capture, mouseover/onclick cell stats, cell family tree, display tics per second, choose and customize three color presets

# heights
play_pause_button_height = .9*world_width*3
add_viruses_button_height = .7*display_height
add_cells_button_height = .5*display_height
add_food_button_height = .3*display_height
reset_button_height = .1*display_height


buttons = {}
button_names = ["play_pause","add_viruses","add_cells","add_food","reset"]
for button_name in button_names:
    buttons[button_name] = Button(button_name,eval(button_name+"_button_height"),eval(button_name+'_img'))

def draw_buttons():
#play_pause_button_xloc = 9*display_width
#cell_designer_button_xloc = .7*display_width
#state_capture_button_xloc = .5*display_width
#family_tree_button_xloc = .3*display_width
#custom_cell_button_xloc = .1*display_width

    #        pygame.draw.circle(windowSurfaceObj, greenColor,(20, 600),9)
    for button in buttons.values():
#                pygame.draw.circle(windowSurfaceObj, greenColor,(int(button.xloc), int(button.height)), int(button.radius))
        windowSurfaceObj.blit(button.image,(int(button.xloc), int(button.yloc)))
#    pygame.display.flip()

def convert_to_display_loc(pos):
        '''change our system of coordinates into coordinates that pygame can understand'''
        # pos contains a tuple of ( 0.0x, 0.0y)
        return int(pos.x*world_width), int(pos.y*world_height)

def convert_envi_loc(display_loc):
        ''' change pygame coordiantes to the format used by the rest of our program'''
        return display_loc[0]/float(world_width),display_loc[1]/float(world_height)

class Display(Thread):

        running_bool = True
                
	# self -> displayobject cell -> circle, radius -> radius, color
	def draw_wrapping_circle(self, circle, radius, color):
		# self is a display object, circle is a cell, radius and color are attributes of that cell

		# real_x, real_y refers to the actual display coordinates of a cell
		real_x, real_y = convert_to_display_loc(circle.pos)

		# make a list that conatins the real display coordinate. This list will later be used to display both the half that isn't cut off and the half tthat appears on the other side of the window
		x_all = [real_x]
		y_all = [real_y]

		# if cell is on the edge of the screen (split halfway?) then append to the list of parts of the cell to be displayed a part on the other half of the screen
		if circle.pos.x < radius:
			x_all.append(world_width + real_x)
		elif circle.pos.x > 1 - radius:
			x_all.append(real_x - world_width)
		if circle.pos.y < radius:
			y_all.append(world_height + real_y)
		elif circle.pos.y > 1 - radius:
			y_all.append(real_y - world_height)

		# display all portions of the cell when it's split between two sides
		for x in x_all:
			for y in y_all:
				pygame.draw.circle(windowSurfaceObj, color,(x, y), int(radius*display_width))

        def draw_wrapping_square(self, square, radius, color):
                real_x, real_y = convert_to_display_loc(square.pos)

                x_all = [real_x]
                y_all = [real_y]

                if square.pos.x < radius:
                        x_all.append(display_width + real_x)
                elif square.pos.x > 1 -radius:
                        x_all.append(real_x - display_width)
                if square.pos.y < radius:
                        y_all.append(display_height + real_y)
                elif square.pos.y > 1 -radius:
                        y_all.append(real_y - display_height)
                for x in x_all:
                        for y in y_all:
                                pygame.draw.rect(windowSurfaceObj, color, (x,y,radius,radius) , 0)
                
# these commented commands will draw hollow cells should we desire to make them hollow
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width), color)
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width+.1), color)
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width+.2), color)
				
				
	def run(self):
		while True:
			# make the background white
			windowSurfaceObj.fill(whiteColor)
			pygame.draw.rect(windowSurfaceObj, blackColor, (.35*3*world_width,0,10,display_height))

			# World's food set is changing while the for loop runs, so we must lock it so that we do not iterate over a changing set
			World.lock.acquire()
			for food in World.food_set:
				
				# convert the food coordinates too coordinates that pygame can understand
				x, y = convert_to_display_loc(food.pos)

				# draw the food circles
				pygame.gfxdraw.filled_circle(windowSurfaceObj, x, y, int(0.01*display_width), redColor)

			# draw all the cells
			for cell in World.cell_list:
				sys.stderr.write("")
				if isinstance(cell, Virus):
                                        #draw virus
                                        self.draw_wrapping_square(cell, 5, pygame.Color(*cell.color))
                                else:
                                        self.draw_wrapping_circle(cell, cell.radius, pygame.Color(*cell.color))
			# we're no longer going through the cell list, so now allow other parts of this project to change the cell list
			World.lock.release()

			# exit if the user says to
			for event in pygame.event.get():
				if event.type ==QUIT:
					pygame.quit()
					return ()
				# add food or cell via left/right mouse click
				elif event.type == MOUSEBUTTONDOWN:
#					print "mouse button down"
					if event.button == 1:
#						print "got position"
						pos = Position(convert_envi_loc(event.pos))
						for button in buttons:
							if math.sqrt(((buttons[button].xloc-event.pos[0])**2)+((buttons[button].yloc-event.pos[1])**2)) < 30:
#								print "button clicked"
								buttons[button].click()
							else:
								if event.pos[0]<world_width and event.pos[1]<world_height:
#									print "adding food at", event.pos
									environment.add_food_at_location(pos)	
						
					elif event.button == 2:
#						print "adding virus"
						pos = Position(convert_envi_loc(event.pos))
						environment.add_virus_at_location(1,pos)
					elif event.button == 3:
#						print "adding cell"
						pos = Position(convert_envi_loc(event.pos))
						environment.add_cell_at_location(pos)
				
				# allow user to change resistance
				# increase resistance if the user hits the U
				elif event.type ==KEYDOWN:
					if event.key == K_u:
						World.resistance +=1000

					# decrease resistance if the user hits D
					# prevent them from making resistance negative
					elif event.key == K_d:
						new_resistance = World.resistance - 250
						if new_resistance >=0:
							World.resistance = new_resistance
						else:
							pass

			# update the screen
			draw_buttons()
			pygame.display.update()
			
