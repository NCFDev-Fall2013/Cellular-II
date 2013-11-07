#	Main function for Cellular II
#	Version 1.3
			
#	DEPENDENCIES: pygame	

#====Built-in Modules====#
import sys, copy

#====Required Modules====#
import pygame

#=====Custom Modules=====#
#from environment import World
import environment
import food, cells, display

World = environment.World

def main():
	"""Runs Cellular II"""
	#Retrieve user input from command line
 	
#	If dash in is input as first arg to Cellular II, default to 100 for food and cell count

#	System arguments numbering starts from python command, e.g. { python Cellular-II.py $foo $bar } 
#	where $1 is Cellular-II.py $2 is $foo and $3 is $bar

	if len(sys.argv) == 2 and sys.argv[1] == '-':	#Evaluates for the case: { python Cellular-II.py - } (one arg && arg=='-')
		starting_food_count = 100		
		starting_cell_count = 100

	elif len(sys.argv) == 3:			#Evaluates for the case: { python Cellular-II.py $2 $3 } (two args)
		starting_food_count  = int(sys.argv[1])
		starting_cell_count  = int(sys.argv[2])
	else:						#Evaluates for the case { python Cellular-II.py } (no args) unexpected number of args
		starting_food_count = input('Enter starting amount of food: ')
		starting_cell_count = input('Enter starting amount of cells: ')


#	Add the proper number of Cells and Food
	environment.add_food(starting_food_count)
	environment.add_cells(starting_cell_count)
	
# 	Where dis is a thread 
	dis = display.Display()
	dis.start()

#	Initial Tick
	worldClock = pygame.time.Clock()
	
	i = 0						#Tick Counter

#						###MAIN LOOP BEGIN###
	while True:
		i += 1
#		If the user closes pygame, close the rest of the program
		if dis.isAlive() == False:		#If thread is stopped, isAlive() evaluates False
			sys.exit()

#		Terminal output	
#		print 'Tick:',i,'\t\tfood: ',len(World.food_set),'\t\tcells: ',len(World.cell_list)
#		print 'Resistance: ', World.resistance

		(worldClock.tick(60) + 0.00000000001)
		World.tick()
#						###MAIN LOOP END###

# 	Closes the graphics thread if the main loop is broken
	dis._Thread__stop()


#Runs above function	
main()
