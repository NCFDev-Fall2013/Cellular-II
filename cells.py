import unittest, environment, random, math, weakref
from vector import Vector, Point
from functools import partial
from operator import itemgetter, attrgetter

def call(a, f):
	"""Unknown function usage. Called within __init__"""
	return f(a)
	
def random_color():
	"""Returns tuple containing color index"""
	randomcolor = random.randint(0,155),int(random.randint(0,155)/1.15),random.randint(0,155)
	return randomcolor

class Cell:
	def __init__(self, x, y,  mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, Phenotype=[2.0, 0.001, 0.5,0.6, 0.005, None, 0.0]):
		"""Cells begin with a specified position, without velocity, task or destination."""
		# Position, Velocity and Acceleration vectors:
		self.pos = Point(float(x), float(y))
		self.vel = Vector(x_vel, y_vel)
		self.acl = Vector(0.0, 0.0)

		# Phenotypes:
		self.phenotype			= Phenotype		# Stored for calc_variance's sake
		self.emRatio			= Phenotype[0]		# Energy/Mass gain ratio
		self.walk_force			= Phenotype[1]
		self.div_energy			= Phenotype[2]		# How much energy a cell needs to divide
		self.div_mass			= Phenotype[3]		# How much mass a cell needs to divide
		self.density			= Phenotype[4]
		if Phenotype[5] == None:
			self.color = random_color()
			Phenotype[5] = self.color
		else:	self.color		= Phenotype[5]
		self.mutation_chance		= Phenotype[6]		# The likelihood of each phenotype mutating
		
		# Required for motion:
		self.energy		 = energy
		self.mass		 = mass
		self.exerted_force	 = Vector(0.0, 0.0)
		self.weight_management()

		# Required for logic:
		self.task		 = None
		self.destination	 = None
		self.destination_type	 = None

		# Task jumptable:
		self.TaskTable			= {}
		self.TaskTable[None]		= self.task_none
		self.TaskTable["FindingFood"]	= self.task_finding_food
		self.TaskTable["GettingFood"]	= self.task_getting_food

	#"Task" functions, i.e. the cell's activities during each tick, depending on its task.
	def task_none(self):
		"""What the cell does should it have no task."""
		self.task = "FindingFood"

	def task_finding_food(self):
		#closest piece of food
		close_food = environment.Environment().food_at(self.pos, self.sight_range)
		#If there is any food within distance self.sight_range, get the closest one.
		if len(close_food) > 0:
			closest_food = min(close_food, key = partial(reduce, call, (attrgetter("pos"), attrgetter("distance_to"), partial(call, self.pos))))# food: self.pos.distance_to(food.pos))
		else: closest_food = None

		if len(close_food) == 0:
			"""What the cell does should it be looking for food."""
			#If you can't see food, accelerate in a random direction.
			x = random.uniform(0, environment.Environment().width)
			y = random.uniform(0, environment.Environment().height)
			self.destination = Point(x, y)
			self.destination_type  = "Exploration"
			self.calc_force()
		else:
			#If there is any food within distance SIGHT_RANGE, get the closest one.
			#closest_food = min(close_food, key = lambda food: self.pos.distance_to(food.pos))
			closest_food = min(close_food, key = partial(reduce, call, (attrgetter("pos"), attrgetter("distance_to"), partial(call, self.pos))))# food: self.pos.distance_to(food.pos))
			
			def stop_getting_food(food):
				"""After the food gets eaten, stop trying to get it."""
				self.destination = self.destination_type = self.task = None
			self.task = "GettingFood"
			self.destination_type = "Food"
			#weakref.proxy calls stop_getting_food when the food is destroyed.
			self.destination = weakref.proxy(closest_food.pos, stop_getting_food)
			self.food_target = weakref.ref(closest_food)

	def task_getting_food(self):
		"""What the cell does when it has found food and is attempting to get it."""
		#assert(len(environment.Environment().food_at(self.destination, 0)) != 0)
		distance_to_destination = self.pos.distance_to(self.destination)
		print self.destination
		print distance_to_destination
		if distance_to_destination > self.distance_to_start_slowing_down():
			self.calc_force()
		
		for f in environment.Environment().food_at(self.pos, self.radius):
			self.eat(f)
		#if distance_to_destination <= self.radius:
		#	self.eat(self.food_target())

	def update_coords(self):
		"""Updates the cell's position, velocity and acceleration in that order."""
		prev_vel = Vector(self.vel.x, self.vel.y)
		
		self.pos += self.vel
		self.vel += self.acl
		#acl is change in velocity
		#displacement = (prev_vel + self.exerted_force/self.mass/2)
		#self.energy -= self.exerted_force*displacement
		#self.energy -= self.exerted_force*prev_vel
		self.acl = self.exerted_force - self.vel*abs(self.vel)*environment.Environment().resistance*(self.radius)/self.mass
		self.exerted_force = Vector(0.0,0.0)

	def calc_force(self):
		"""Cells calculate how much force they are exerting (prior to resistance)."""
		self.exerted_force = (self.destination - self.pos)*self.walk_force / abs(self.destination - self.pos)
		#self.exerted_force = (self.destination - self.pos)*self.walk_force / (abs(self.destination - self.pos)*self.mass)
		if self.energy > self.walk_force:
			self.energy -= self.walk_force*1.0
		else:
			self.mass -= self.walk_force*3.0

	def distance_to_start_slowing_down(self):
		"""Calculates the distance from the destination that, once past,
		the cell ought to begin slowing down to reach its destination."""
		return (abs(self.vel) * self.mass) / (environment.Environment().resistance * self.radius)

	def eat(self, f):
		"""Updates energy and mass according to set emRatio value and removes food item."""
		#for f in environment.Environment().food_at(self.pos, self.radius):
		self.energy += f.energy/self.emRatio
		self.mass += f.energy - (f.energy/self.emRatio)
		environment.Environment().remove_food(f)
		#The above line automatically resets our task and destination by calling stop_getting_food()

	def weight_management(self):
		"""Updates radius and sight range according to mass and density"""
		self.radius = ( 3.0*self.mass*self.density / (4.0*math.pi) )**(1/2.0)
		self.sight_range = .2 + self.radius

	def calculate_variance(self):
		"""Setting variance for child cell. Called when cell duplicates""" #Currently only color varaince 
		newphenotype = []
		##Below code needs to be rewritten##
		###SOLUTION: Use fraction of acceptable margin as argument for randint modification###
		newcolor = (self.phenotype[5][0] + random.randint(-15,15),self.phenotype[5][1] + random.randint(-15,15), +\
			    self.phenotype[5][2] + random.randint(-15,15))
		
		while (newcolor[0]+newcolor[1]+newcolor[2])/3>150 or newcolor[0]<0 or newcolor[0]>255 or newcolor[1]<0 or newcolor[1]>255 or newcolor[2]<0 or newcolor[2]>255:
			newcolor = (self.phenotype[5][0]+random.randint(-15,15), int(self.phenotype[5][1]+random.randint(-15,15)/1.15), self.phenotype[5][2]+random.randint(-15,15))
		for t in self.phenotype[:5]:	newphenotype.append(t)
		newphenotype.append(newcolor)
		for t in self.phenotype[6:]:	newphenotype.append(t)
		return newphenotype

	def life_and_death(self):
		"""Checks if cell mass is great enough for division or low enough to cause death.""" 
		"""Brings new cells into existance or removes cell if conditions are true."""
		if self.mass >= self.div_mass and self.energy >= self.div_energy:
			##Removed Jack-ese##			
			#Statistics for child cells
			newMass		= self.mass/self.emRatio
			newEnergy	= (self.energy - 3.0)/self.emRatio

			#Create child 1
			x1 = random.uniform(self.pos.x-0.01,self.pos.x+0.01)
			y1 = random.uniform(self.pos.y-0.01,self.pos.y+0.01)
			newPhenotype1	= self.calculate_variance()
			environment.Environment().cell_list.append(Cell(x1,y1,newMass,newEnergy,self.vel.x,self.vel.y,newPhenotype1))
			
			#Create child 2
			x2 = random.uniform(self.pos.x-0.01,self.pos.x+0.01)
			y2 = random.uniform(self.pos.y-0.01,self.pos.y+0.01)
			newPhenotype2	= self.calculate_variance()
			environment.Environment().cell_list.append(Cell(x2,y2,newMass,newEnergy,self.vel.x,self.vel.y,newPhenotype2))
						
			#Instantiates children at slightly different positions
			environment.Environment().remove_cell(self)
		#Kills cell
		elif self.mass <= 0.1:

                               

			
	def one_tick(self):
		"""What a cell does every arbitrary unit of time."""
		self.TaskTable[self.task]()
		self.update_coords()
		self.weight_management()
		self.life_and_death()
		#cell_col_list = environment.Environment().cell_list
		#self.collision_detection(cell_col_list, self.x, self.y, self.radius)
                
