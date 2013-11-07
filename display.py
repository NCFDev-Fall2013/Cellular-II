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

# i'm pretty sure we don't need this
#mousex, mousey = 0,0



# start a thread so that we can later prevent environment from changing the list of cells while we interate through it
Thread = threading.Thread

# starts pygame
pygame.init()

# i don't think we need this
#fpsClock = pygame.time.Clock()

# set dimensions of display window
display_width = 500
display_height = 500
windowSurfaceObj = pygame.display.set_mode((display_width,display_height))

#window title
pygame.display.set_caption('Nautical Cell Force 2')


def convert_to_display_loc(pos):
	'''change our system of coordinates into coordinates that pygame can understand'''
	# pos contains a tuple of ( 0.0x, 0.0y)
	return int(pos.x*display_width), int(pos.y*display_height)

def convert_envi_loc(display_loc):
	''' change pygame coordiantes to the format used by the rest of our program'''
	return display_loc[0]/float(display_width),display_loc[1]/float(display_height)

class Display(Thread):
        

	def __init__(self,environment):
		Thread.__init__(self)
		self.environment = environment
                self.running_bool = True
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
			x_all.append(display_width + real_x)
		elif circle.pos.x > 1 - radius:
			x_all.append(real_x - display_width)
		if circle.pos.y < radius:
			y_all.append(display_height + real_y)
		elif circle.pos.y > 1 - radius:
			y_all.append(real_y - display_height)

		# display all portions of the cell when it's split between two sides
		for x in x_all:
			for y in y_all:
				pygame.draw.circle(windowSurfaceObj, color,(x, y), int(radius*display_width))

# these commented commands will draw hollow cells should we desire to make them hollow
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width), color)
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width+.1), color)
#				pygame.gfxdraw.aacircle(windowSurfaceObj, x, y, int(radius*display_width+.2), color)
				
				
	def run(self):
		while True:
			# make the background white
			windowSurfaceObj.fill(whiteColor)

			# environment's food set is changing while the for loop runs, so we must lock it so that we do not iterate over a changing set
			self.environment.lock.acquire()
			for food in self.environment.food_set:
				
			# convert the food coordinates too coordinates that pygame can understand
				x, y = convert_to_display_loc(food.pos)

				# draw the food circles
				pygame.gfxdraw.filled_circle(windowSurfaceObj, x, y, int(0.01*display_width), redColor)

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
					elif event.key == K_p:
                                                if self.running_bool == True: self.running_bool = False
                                                else: self.running_bool = True

			# update the screen
			pygame.display.update()

# i don't think we need this
#			fpsClock.tick(60)

def display(environment):
	dis = Display(environment)
	dis.start()
	# return the thread so that main can check if it is alive
	return dis
