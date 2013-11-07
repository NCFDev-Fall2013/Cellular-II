#	Main function for Cellular II
#	Version 1.1
			
#	DEPENDENCIES: pygame, cffi	

#=====Import List=====#
import environment
import food
import cells
import copy
import sys
import display
import pygame
#====End of Imports===#

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
##		continue_passing_args = raw_input('Do you want to modify other things? y/n  ')
##		if continue_passing_args == "y":
##			sim_speed = input('Enter simulation speed (60 = fast, 15 = slow): ')            #Controls simulation speed
##			add_food_rate = input('Enter desired food reseed probability: (normal: 10) ')   #Controls food reseed probability
##			usr_resist = input('Enter world resistance (normal: 600): ')                    #Controls world resistance
##		else:
##			sim_speed = 45
##			add_food_rate = 10
##			usr_resist = 600


#	Initialize World Object	
	World = environment.Environment(starting_food_count,starting_cell_count)
	
# 	Where dis is a thread 
	dis = display.display(World)

#	Initial Tick
	worldClock = pygame.time.Clock()
	
	i = 0						#Tick Counter

#						###MAIN LOOP BEGIN###
        print "Beginning Loop"
	while True:
                if dis.isAlive() == False:		#If thread is stopped, isAlive() evaluates False
                                sys.exit()

                while dis.running_bool:
                        #print "running is ", dis.running_bool
                        i += 1
        #		If the user closes pygame, close the rest of the program
                        
        #		Terminal output	
                        print 'Tick:',i,'\t\tfood: ',len(World.food_set),'\t\tcells: ',len(World.cell_list)
                        print 'Resistance: ', environment.Environment().resistance

        #					###----------Obsolete Code----------###
        #		#print 'Tick: ',i,'\t\tfood: ',len(World.food_set),'\t\tcells: ',len(World.cell_list)
        #		#print 1000/
        #					###--------END Obsolete Code--------###


                        (worldClock.tick(60) + 0.00000000001)
                        World.tick()
                #if not dis.running_bool:
                        #where dropbox stat functionality would be

        #print "unreachable?"
                        
#						###MAIN LOOP END###

# 	Closes the graphics thread if the main loop is broken
	dis._Thread__stop()
	


#Runs above function	
main()
