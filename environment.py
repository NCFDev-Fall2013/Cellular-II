# prevent anyone from running environment.py directly
if __name__ == "__main__": print 'no'; exit(-1)

import cells, food, random, unittest, singleton, vector, threading, math

class Environment(singleton.Singleton):
	def init_once(self, food_count, cells_count, add_food_rate=10, usr_resist=600):
		"""Generate a 1x1 environment with specified amount of food and cells"""
		self.cell_list = []
		self.food_set = set()
		self.lock = threading.Lock()
		self.width = self.height = 1.0
		self.add_food(food_count)
		self.add_cells(cells_count)
		self.turn = 0
		self.reseed_prob = add_food_rate
		self.resistance = usr_resist

	def add_food(self, food_count):
		"""Add food_count number of foods at random locations"""
		for i in range(food_count):
			self.food_set.add(food.Food(random.uniform(0, self.width), random.uniform(0, self.height)))
	def add_food_at_location(self, pos):
		"""Add a food item at location"""
		self.food_set.add(food.Food(pos.x, pos.y))

	def add_cells(self, cell_count):
		''' Add cell_count number of cells of random colors at random locations to the world'''
		for i in range(cell_count):
			self.cell_list.append(cells.Cell(random.uniform(0, self.width), random.uniform(0, self.height)))
			
	def add_cell_at_location(self, pos):
		"""Add a cell at location"""
		self.cell_list.append(cells.Cell(pos.x, pos.y))

	def add_specific_cell_at_location(self, cell, pos)
                self.cell_list.append(cell(pos.x, pos.y))

        def collision_detection(self, cell_list_initial):
                cell_list_clone = cell_list_initial[:]
                for cell_A in cell_list_initial:
                        cell_list_clone.remove(cell_A)
                        for cell_B in cell_list_clone:
                               if  math.sqrt((cell_B.pos.x - cell_A.pos.x)**2 + (cell_B.pos.y - cell_A.pos.y)**2) <= (cell_B.radius + cell_A.radius):
                                        print "OMG WE'RE TOUCHING ZOMG"
##                                        cell_A.vel = vector.Vector(0,0)
##                                        cell_B.vel = vector.Vector(0,0)
##                                        cell_A.acl = vector.Vector(0,0)
##                                        cell_B.acl = vector.Vector(0,0)
                                        cell_A.collideWith(cell_B)
                                        cell_B.collideWith(cell_A)
                                        
	def tick(self):
		''' give each cell a turn and maybe add food to the world'''
		# we need to lock the cell_list so that we can itterate through it
                
		self.lock.acquire()
                
                
		for cell in self.cell_list:
			cell.one_tick()
			
		# There is reseed_prob chance that a food item is added to the word at a random place.
		if random.randint(0,100)<=self.reseed_prob:
			self.add_food(1)

		self.turn += 1
		
		# maybe we can move this up before food is added?
		self.lock.release()
                

	def food_at(self, pos, r):
		'''return list of food within distance r of position pos'''
		return [food for food in self.food_set if pos.distance_to(food.pos) <= r]

	def remove_food(self, food):
		'''delete a food item'''
		try:
			self.food_set.remove(food)

		# handle food having already been removed
		except KeyError:
			pass

	def remove_cell(self,cell):
		''' delete a cell'''
		self.cell_list.remove(cell)
		
	def kill_cell(self,cell):
		''' replaces a cell with food'''
		self.cell_list.remove(cell)
		self.add_food_at_location(cell.pos)

	# print_table()
	#	output a table of each cell state to a text file

	def print_table(self,filename,comment=""):
		"""Prints a table to a textfile with the provided name, with the provided comment above it."""
		''' Data: Cell placement, velocity, acceleration destination, radius, energy, mass, task'''
		table_file = open(filename,"a")
		# Header
		table_file.write("\n"+str(comment)+"\nCell_n\tx_pos\ty_pos\tx_vel\ty_vel\tx_acl\ty_acl\tx_dest\ty_dest\tradius\tenergy\tmass\ttask\n")
		counter = 0
		for cell in self.cell_list:
			# Beginning of the row
			table_file.write("Cell_"+str(counter)+"\t"+str(round(cell.pos.x,4))+"\t"+str(round(cell.pos.y,4))+"\t"+\
			str(round(cell.vel.x,4))+"\t"+str(round(cell.vel.y,4))+"\t"+str(round(cell.acl.x,4))+"\t"+str(round(cell.acl.y,4)))

			# Destination issues; need the if/elif for when destination is just Nonetype
			if type(cell.destination) == type(None):
				table_file.write("None\tNone\t")
			elif cell.destination.__class__ == vector.Point:
				table_file.write(str(round(cell.destination.x,4))+"\t"+str(round(cell.destination.y,4))+"\t")
			else: raise TypeError(str(type(cell.destination))+" "+str(cell.destination))

			# Back to the rest of the row
			table_file.write("%7.3f %7.3f %7.3f" %  (cell.radius, cell.energy, cell.mass))
			#table_file.write(str(round(cell.radius,4))+"\t"+str(round(cell.energy,4))+"\t"+str(round(cell.mass,4))+\
			#"\t"+str(cell.task)+"\n")

			counter += 1
		table_file.close()

        def add_food(self, food_count):
                """Add food_count number of foods at random locations"""
                for i in range(food_count):
                        self.food_set.add(food.Food(random.uniform(0, self.width), random.uniform(0, self.height)))
        def add_food_at_location(self, pos):
                """Add a food item at location"""
                self.food_set.add(food.Food(pos.x, pos.y))

        def add_cells(self, cell_count):
                ''' Add cell_count number of cells of random colors at random locations to the world'''
                for i in range(cell_count):
                        self.cell_list.append(cells.Cell(random.uniform(0, self.width), random.uniform(0, self.height)))

        def add_cells(self, cell_count, cell, pos):
                ''' Add cell_count number of cells of random colors at random locations to the world'''
                for i in range(cell_count):
                        cell.x = pos.x * random.random()
                        cell.y = pos.y * random.random()
                        self.cell_list.append(cell)

                        
        def add_cell_at_location(self, pos):
                """Add a cell at location"""
                self.cell_list.append(cells.Cell(pos.x, pos.y))

        def add_specific_cell_at_location(self, cell, pos):
                """Add a cell at location"""
                cell.pos = pos
                self.cell_list.append(cell)
                        
        def tick(self):
                ''' give each cell a turn and maybe add food to the world'''
                # we need to lock the cell_list so that we can itterate through it
                self.lock.acquire()

                print "@_____@"
                #print "ATTEMPTING COLLISION"
                self.collision_detection(self.cell_list)
                
                for cell in self.cell_list:
                        cell.one_tick()
                        
                # There is reseed_prob chance that a food item is added to the word at a random place.
                if random.randint(0,100)<=self.reseed_prob:
                        self.add_food(1)
                self.turn += 1
                
                # maybe we can move this up before food is added?
                self.lock.release()

        def food_at(self, pos, r):
                '''return list of food within distance r of position pos'''
                return [food for food in self.food_set if pos.distance_to(food.pos) <= r]

        def remove_food(self, food):
                '''delete a food item'''
                try:
                        self.food_set.remove(food)

                # handle food having already been removed
                except KeyError:
                        pass

        def remove_cell(self,cell):
                ''' delete a cell'''
                self.cell_list.remove(cell)
                
        def kill_cell(self,cell):
                ''' replaces a cell with food'''
                self.cell_list.remove(cell)
                self.add_food_at_location(cell.pos)

        # print_table()
        #       output a table of each cell state to a text file

        def print_table(self,filename,comment=""):
                """Prints a table to a textfile with the provided name, with the provided comment above it."""
                ''' Data: Cell placement, velocity, acceleration destination, radius, energy, mass, task'''
                table_file = open(filename,"a")
                # Header
                table_file.write("\n"+str(comment)+"\nCell_n\tx_pos\ty_pos\tx_vel\ty_vel\tx_acl\ty_acl\tx_dest\ty_dest\tradius\tenergy\tmass\ttask\n")
                counter = 0
                for cell in self.cell_list:
                        # Beginning of the row
                        table_file.write("Cell_"+str(counter)+"\t"+str(round(cell.pos.x,4))+"\t"+str(round(cell.pos.y,4))+"\t"+\
                        str(round(cell.vel.x,4))+"\t"+str(round(cell.vel.y,4))+"\t"+str(round(cell.acl.x,4))+"\t"+str(round(cell.acl.y,4)))

                        # Destination issues; need the if/elif for when destination is just Nonetype
                        if type(cell.destination) == type(None):
                                table_file.write("None\tNone\t")
                        elif cell.destination.__class__ == vector.Point:
                                table_file.write(str(round(cell.destination.x,4))+"\t"+str(round(cell.destination.y,4))+"\t")
                        else: raise TypeError(str(type(cell.destination))+" "+str(cell.destination))

                        # Back to the rest of the row
                        table_file.write("%7.3f %7.3f %7.3f" %  (cell.radius, cell.energy, cell.mass))
                        #table_file.write(str(round(cell.radius,4))+"\t"+str(round(cell.energy,4))+"\t"+str(round(cell.mass,4))+\
                        #"\t"+str(cell.task)+"\n")

                        counter += 1
                table_file.close()

class CreationTest(unittest.TestCase):
        ''' unit tests'''
        def runTest(self):
                ''' run unit tests'''
                #environment already initialized in test.py
                environment = Environment() 

                # test that environment is a singleton
                self.assertTrue(Environment() is environment)

                # test that environment initializes properly
                self.assertEquals(len(environment.cell_list), 10)
                self.assertEquals(len(environment.food_set), 10)
                self.assertTrue(environment.width > 0)
                self.assertTrue(environment.height > 0)
                
                # test that cells are within bounds
                for cell in environment.cell_list:
                        self.assertTrue(cell.pos.x >= 0 and cell.pos.x <= environment.width and cell.pos.y >= 0 and cell.pos.y <= environment.height, "Cell location out of bounds.")
                # ..and food is within bounds
                for f in environment.food_set:
                        self.assertTrue(f.pos.x >= 0 and f.pos.x <= environment.width and f.pos.y >= 0 and f.pos.y <= environment.height, "Food location out of bounds.")

                environment.cell_list = []
                # test that a cell will find and eat food underneath it
                c = cells.Cell(environment.width/2, environment.height/2)
                environment.cell_list.append(c)
                food_count = len(environment.food_set)

                environment.food_set.add(food.Food(environment.width/2, environment.height/2))          
                environment.tick()
                # test that food list count was decremented after food is eaten
                self.assertEqual(len(environment.food_set), food_count) 
                
                # test that food inside the cell is eaten
                environment.food_set.add(food.Food(environment.width/2 + c.radius - 0.000001, environment.height/2))
                environment.tick()
                self.assertEqual(len(environment.food_set), food_count)

                # test that food outside the cell is not eaten
                environment.food_set.add(food.Food(environment.width/2 + c.radius + 0.000001, environment.height/2))
                environment.tick()
                self.assertEqual(len(environment.food_set), food_count + 1)
                
                # test that add_cells adds the right number of cells
                num_cells = len(environment.cell_list)
                add_cells_count = random.randint(0,100)
                environment.add_cells(add_cells_count)
                self.assertEqual(len(environment.cell_list)-add_cells_count,num_cells)
                

def debug_print_table():
        '''tests print_table by creating a world with set information and then print_tabling that world to make sure the info is accurate'''
        tbl = "Debug_Cell_Table.txt"
        Env = Environment(0,0)
        Env.cell_list.append(Cell(0,0))
        Env.cell_list.append(Cell(1,2))
        Env.cell_list.append(Cell(7,5))
        Env.cell_list.append(Cell(6,9))
        Env.cell_list.append(Cell(-7,-7))
        Env.print_table(tbl)
        Env.tick()
        Env.print_table(tbl)
        Env.tick()
        Env.print_table(tbl)
        for run in xrange(5):
                Env.tick()
        Env.print_table(tbl)
        for run in xrange(50):
                Env.tick()
        Env.print_table(tbl)



