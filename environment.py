# prevent anyone from running environment.py directly
if __name__ == "__main__": print 'no'; exit(-1)

#====Built-in Modules====#
import random, threading, math

#=====Custom Modules=====#
import vector

class Environment(object):
	def __init__(self):
		"""Generate a 1x1 environment with specified amount of food and cells"""
		self.cell_list = []
		self.food_set = set()
		self.lock = threading.Lock()
		self.width = self.height = 1.0
		self.turn = 0
		self.reseed_prob = 10
		self.resistance = 600

        def collision_detection(self, cell_list_initial):
                cell_list_clone = cell_list_initial[:]
                cell_list_doubleClone = cell_list_initial[:]
                for cell_A in cell_list_doubleClone:
                        cell_list_clone.remove(cell_A)
                        for cell_B in cell_list_clone:
                               if  math.sqrt((cell_B.pos.x - cell_A.pos.x)**2 + (cell_B.pos.y - cell_A.pos.y)**2) <= (cell_B.radius + cell_A.radius):
                                        cell_A.collideWith(cell_B)
                                        cell_B.collideWith(cell_A)                        

        def tick(self):
                ''' give each cell a turn and maybe add food to the world'''
                # we need to lock the cell_list so that we can itterate through it
                self.lock.acquire()

                # "@_____@"

                #print "ATTEMPTING COLLISION"
                self.collision_detection(self.cell_list)
                
                for cell in self.cell_list:
                        cell.one_tick()
                        
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
import cells, food, virus


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
                        
def add_cell_at_location(pos):
	"""Add a cell at location"""
	World.cell_list.append(cells.Cell(pos.x, pos.y))

def add_viruses(virus_count):
        ''' Add virus_count number of cells of random colors at random locations to the world'''
        for i in range(virus_count):
                World.cell_list.append(virus.Virus(random.uniform(0, World.width), random.uniform(0, World.height)))

def add_viruses_at_loc(virus_count, loc):
        for i in range(virus_count):
                World.cell_list.append(virus.Virus(loc.x + .01*random.uniform(0, 1), loc.y + .01*random.uniform(0, 1)))

def add_virus(pos):
        World.cell_list.append(virus.Virus(pos.x, pos.y, 1, 1, 4, 4, "on_death_disperse", 50, 2))

def add_specific_cell_at_location(cell, pos):
        cell.pos.x = pos.x
        cell.pos.y = pos.y
        World.cell_list.append(cell)
