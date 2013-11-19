import pygame, sys, threading, environment, random
from pygame.locals import *
import pygame.gfxdraw

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



# start a thread so that we can later prevent environment from changing the list of cells while we interate through it
Thread = threading.Thread

# starts pygame
pygame.init()

# i don't think we need this
#fpsClock = pygame.time.Clock()

# set dimensions of dispnlay window
world_width = 500
world_height = 500
display_width = int(1.3*world_width)
display_height = world_height


windowSurfaceObj = pygame.display.set_mode((display_width,display_height))

#window title
pygame.display.set_caption('Nautical Cell Force 2')


#button class
class Button():
	button_xlocs = .4*world_width*3
	button_radiuses = .05*display_height

	def __init__(self,name,height,image_loc):
		self.name =name
		self.xloc = Button.button_xlocs
		self.image_loc = image_loc
		self.height = height
		self.radius = Button.button_radiuses
#button_locations
#play-pause,settings, cell designer, state capture, mouseover/onclick cell stats, cell family tree, display tics per second, choose and customize three color presets

play_pause_button_height = .9*world_width*3
cell_designer_button_height = .7*display_height
state_capture_button_height = .5*display_height
family_tree_button_height = .3*display_height
custom_cell_button_height = .1*display_height
buttons = {}
button_names = ["play_pause","cell_designer","state_capture","family_tree","custom_cell"]
for button_name in button_names:
	buttons[button_name] = Button(button_name,eval(button_name+"_button_height"),'')



def convert_to_display_loc(pos):
	'''change our system of coordinates into coordinates that pygame can understand'''
	# pos contains a tuple of ( 0.0x, 0.0y)
	return int(pos.x*world_width), int(pos.y*world_height)

def draw_buttons():
#play_pause_button_xloc = 9*display_width
#cell_designer_button_xloc = .7*display_width
#state_capture_button_xloc = .5*display_width
#family_tree_button_xloc = .3*display_width
#custom_cell_button_xloc = .1*display_width

#	pygame.draw.circle(windowSurfaceObj, greenColor,(20, 600),9)
	for button in buttons.values():
		pygame.draw.circle(windowSurfaceObj, greenColor,(int(button.xloc), int(button.height)), int(button.radius))

def convert_envi_loc(display_loc):
	''' change pygame coordiantes to the format used by the rest of our program'''
	return display_loc[0]/float(world_width),display_loc[1]/float(world_height)

class Display(Thread):
	def __init__(self,environment):
		Thread.__init__(self)
		self.environment = environment

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
				pygame.draw.circle(windowSurfaceObj, color,(x, y), int(radius*world_width))

# these commented commands will draw hollow cells should we desire to make them hollow
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width), color)
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width+.1), color)
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width+.2), color)
				
				
	def run(self):
		while True:
			# make the background white
			windowSurfaceObj.fill(whiteColor)
			# first number is how far left
			# second number is height, smaller is higher
			# third number is width
			# fourth number how thick vertically the line is
			draw_buttons()
			pygame.draw.rect(windowSurfaceObj, blackColor, (.35*3*world_width,0,10,display_height))
			
			# environment's food set is changing while the for loop runs, so we must lock it so that we do not iterate over a changing set
			self.environment.lock.acquire()
			for food in self.environment.food_set:
				
			# convert the food coordinates too coordinates that pygame can understand
				x, y = convert_to_display_loc(food.pos)

				# draw the food circles
				pygame.gfxdraw.filled_circle(windowSurfaceObj, x, y, int(0.01*world_width), redColor)

			# draw all the cells
			for cell in self.environment.cell_list:
                                print "",
				#print cell.color
				self.draw_wrapping_circle(cell, cell.radius, pygame.Color(*cell.color))
			# we're no longer going through the cell list, so now allow other parts of this project to change the cell list
			self.environment.lock.release()

			# exit if the user says to
			for event in pygame.event.get():
				if event.type ==QUIT:
					pygame.quit()
					return ()
				# add food or cell via left/right mouse click
				elif event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						pos = Position(convert_envi_loc(event.pos))
						environment.Environment().add_food_at_location(pos)
					elif event.button == 3:
						pos = Position(convert_envi_loc(event.pos))
						environment.Environment().add_cell_at_location(pos)
				
				# allow user to change resistance
				# increase resistance if the user hits the U
				elif event.type ==KEYDOWN:
					if event.key == K_u:
						environment.Environment().resistance +=1000

					# decrease resistance if the user hits D
					# prevent them from making resistance negative
					elif event.key == K_d:
						new_resistance = environment.Environment().resistance - 250
						if new_resistance >=0:
							environment.Environment().resistance = new_resistance
						else:
							pass

			# update the screen
			pygame.display.update()

# i don't think we need this
#			fpsClock.tick(60)

def display(environment):
	dis = Display(environment)
	dis.start()
	# return the thread so that main can check if it is alive
	return dis

