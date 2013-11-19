# prevent anyone from running environment.py directly
if __name__ == "__main__": print 'no'; exit(-1)

#====Built-in Modules====#
import random, threading, math

#=====Custom Modules=====#
import food, vector, familytree

class Environment(object):
	def __init__(self):
		"""Generate a 1x1 environment with specified amount of food and cells"""
		self.total_cells = 0
		self.cell_list = []
		self.food_set = set()
		self.lock = threading.Lock()
		self.width = self.height = 1.0
		self.turn = 0
		self.reseed_prob = 10
		self.resistance = 600

        def collision_detection(self, cell_list_initial):
                cell_list_clone = cell_list_initial[:]
                for cell_A in cell_list_initial:
                        cell_list_clone.remove(cell_A)
                        for cell_B in cell_list_clone:
                               if  math.sqrt((cell_B.pos.x - cell_A.pos.x)**2 + (cell_B.pos.y - cell_A.pos.y)**2) <= (cell_B.radius + cell_A.radius):
                                        cell_A.collideWith(cell_B)
                                        cell_B.collideWith(cell_A)                        

        def tick(self):
                ''' give each cell a turn and maybe add food to the world'''
                # we need to lock the cell_list so that we can itterate through it
                self.lock.acquire()

                #print "ATTEMPTING COLLISION"
                self.collision_detection(self.cell_list)
                
                for cell in self.cell_list:
                        cell.one_tick()
                for cell in familytree.cell_record:
                        print cell,cell_record[cell]
                
                # There is reseed_prob chance that a food item is added to the word at a random place.
                if random.randint(0,100)<=self.reseed_prob:
                        add_food(1)
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
                add_food_at_location(cell.pos)

World = Environment()
import cells


def add_food(food_count):
	"""Add food_count number of foods at random locations"""
	for i in range(food_count):
		World.food_set.add(food.Food(random.uniform(0, World.width), random.uniform(0, World.height)))
def add_food_at_location(pos):
	"""Add a food item at location"""
	World.food_set.add(food.Food(pos.x, pos.y))

def add_cells(cell_count):
	''' Add cell_count number of cells of random colors at random locations to the world'''
	for i in range(cell_count):
		World.cell_list.append(cells.Cell(random.uniform(0, World.width), random.uniform(0, World.height)))
		# Adds the cell ID to the list of origin cells
		familytree.origin_cells.append(str(World.total_cells))
		World.total_cells += 1
                        
def add_cell_at_location(pos):
	"""Add a cell at location"""
	World.cell_list.append(cells.Cell(pos.x, pos.y))
	# Adds the cell ID to the list of origin cells
	familytree.origin_cells.append(str(World.total_cells))
	World.total_cells += 1
