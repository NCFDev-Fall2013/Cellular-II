#=======================Built-in Modules=======================#
import numpy
from functools import partial
from operator import itemgetter, attrgetter
import random, math, weakref

#========================Custom Modules========================#
import environment
World = environment.World
from vector import Vector, Point
from config import Settings
settings = Settings()

def call(a, f): return f(a)

class Colors():
	def __init__(self):
		self.colorGroups = ['default','user1','user2','user3']
		self.colorList = []
		self.genColorList()

	def genColorList(self):
		section = settings.getValue('COLORS','selectSet',1)
                if section is 0: self.colorList = settings.getValue('COLORS','default',3)
		if section is 1: self.colorList = settings.getValue('COLORS','user1',3)
		if section is 2: self.colorList = settings.getValue('COLORS','user2',3)
		if section is 3: self.colorList = settings.getValue('COLORS','user3',3)

	def genColor(self):
		if len(self.colorList) is 0: self.genColorList()
		pos = random.randint(0,(len(self.colorList)-1))
		return self.colorList.pop(pos)

class AI(object):
	"""AI for cell"""
	def __init__(self, div_energy=0.5, div_mass=0.6, mutation_chance=30, density=0.005, emRatio=2.0,):
		self.div_energy=div_energy
		self.div_mass=div_mass
		self.mutation_chance=mutation_chance
		self.density=density
		self.color=None
		self.emRatio=emRatio
	
	def mutate_AI(self):
		self.div_energy=mutate(self.div_energy, 0, 100, 0.1)
		self.div_mass=mutate(self.div_mass,0,100,.01)
		self.mutation_chance=mutate(self.mutation_chance,0,100,1)
		self.density = mutate(self.density,0,10,.001)
		self.emRatio=mutate(self.emRatio,1,100,.1)


class Static(object):
	"""Attributes that take take a set amount of energy"""
	def __init__(self, walk_force=0.001):
		self.walk_force=walk_force
	def mutate_Static(self):
		self.walk_force=mutate(self.walk_force,0,10,.001)
		

class Dynamic(object):
	"""Attributes that take a percentage base of energy"""
	def __init__(self, run_force=0.01):
		self.run_force=run_force
	def mutate_Dynamic(self):
		self.run_force=mutate(self.run_force,0,100,.01)

class Phenotype(object):
	def __init__(self, _AI=None, _Static=None, _Dynamic=None):
		if not _AI:
			self.AI=AI()
		else:
			self.AI= _AI

		if not _Static:
			self.Static=Static()
		else:
			self.Static=_Static

		if not _Dynamic:
			self.Dynamic=Dynamic()
		else:
			self.Dynamic= _Dynamic

	def mutate_phenotype(self):
		self.AI.mutate_AI()
		self.Static.mutate_Static()
		
def mutate(value, lower, upper, maxincrement):
        variation=random.uniform(-maxincrement,maxincrement)
        if value+variation >=upper or value+variation<= lower:
                return mutate(value,lower,upper,maxincrement)
        else:
                return value+variation
		
def mutateColor(rgbTuple = None):
	"""creates a random color based on provided tuple"""
	if rgbTuple is None:
		x = [random.randomint(0,255) for x in range(3)]
		return tuple(x)
	amounts	= []
	amount 	= [0,0,0]
	rgbList	= list(rgbTuple)
	fullMutate = settings.getValue('COLORS', 'allChange', 1)
	changeMagnitude = settings.getValue('COLORS', 'magnitude', 1)
	if changeMagnitude != 0:
		for value in amount:
			while value is 0: value = random.randint(-changeMagnitude,changeMagnitude)
		amounts.append(value)
	'''
	decides whether or not each value changes
	#0-2: single color change - (0-r,   1-g,   2-b)
	#3-5: double color change - (3-rg,  4-rb,  5-gb)
	#6-8: single color change - (6-r,   7-g,   8-b)
	#9-?: triple color change - (9-? - rgb)
	'''
	mutate = random.randint(0,8+fullMutate)
	if   (mutate >= 0) and (mutate <= 2): rgbList[mutate]	+= amounts[mutate]
	elif (mutate >= 6) and (mutate <= 8): rgbList[mutate-6] += amounts[mutate-6]
	elif (mutate == 3) or  (mutate == 4): rgbList[0] += amounts[0]
	elif (mutate == 3) or  (mutate == 5): rgbList[1] += amounts[1]
	elif (mutate == 4) or  (mutate == 5): rgbList[2] += amounts[2]
	elif (mutate >=9): rgbList = [rgbList[x]+amounts[x] for x in range (3)]
	rgbList = [0 if value < 0 else 255 if value > 255 else value for value in rgbList]
	return tuple(rgbList)

# We need to create a default pheontype
# This is because when cells are created they are given phenotype objects
# And these phenotype objects do not seem to be a constant, default value
# i.e. as the program runs, brand new cells are given mutated phenotypes
# default_phenotype()
# Big cells BAD
# Little cellls BAD
# we need to make the distance_to_slow_down variable a mutation ( I think)
# and we need to deincentivize large cells
# we also may need to fix sight ranges for large cells
# and we ought to change the bounds for reproductive requirements
# so cells don't stay forever huge

class Cell(object):
	colors = Colors()
	def __init__(self, x, y,  mass=0.3, energy=0.1, x_vel=0.0, y_vel=0.0, inherited_phenotype=Phenotype()):
		"""Cells begin with a specified position, without velocity, task or destination."""
		# Position, Velocity and Acceleration vectors:
		self.pos = Point(float(x), float(y))
		self.vel = Vector(x_vel, y_vel)
		self.acl = Vector(0.0, 0.0)

                # Brad's Satisfaction
                self.keyList = []
                for i in range(0,9):
                        self.keyList.append([])
                        for j in range (0,9):
                                self.keyList[i].append(False)

		# Phenotypes:
		self.phenotype		= inherited_phenotype		# Stored for calc_variance's sake
		self.emRatio		= inherited_phenotype.AI.emRatio	# Energy/Mass gain ratio
		self.div_energy		= self.phenotype.AI.div_energy	# How much energy a cell needs to divide
		self.div_mass		= self.phenotype.AI.div_mass		# How much mass a cell needs to divide
		self.walk_force		= self.phenotype.Static.walk_force
		self.density		= self.phenotype.AI.density
		self.mutation_chance	= self.phenotype.AI.mutation_chance	# The likelihood of each phenotype mutating
		if self.phenotype.AI.color == None: self.color = Cell.colors.genColor()
		else: self.color = mutateColor(self.phenotype.AI.color)
		# Required for motion:
		self.energy		= energy
		self.mass		= mass
		self.exerted_force	= Vector(0.0, 0.0)
		self.weight_management()

		# Required for logic:
		self.task		= None
		self.destination	= None
		self.destination_type	= None

		# Task jumptable:
		self.TaskTable			= {}
		self.TaskTable[None]		= self.task_none
		self.TaskTable["FindingFood"]	= self.task_finding_food
		self.TaskTable["GettingFood"]	= self.task_getting_food

	#"Task" functions, i.e. the cell's activities during each tick, depending on its task.
	def task_none(self):
		"""What the cell defaults to in the instance of having no task."""
		self.task = "FindingFood"

	def task_finding_food(self):
		#closest piece of food
		close_food = World.food_at(self.pos, self.sight_range)
		#If there is any food within distance self.sight_range, get the closest one.
		if len(close_food) > 0:
			closest_food = min(close_food, key = partial(reduce, call, (attrgetter("pos"), attrgetter("distance_to"), partial(call, self.pos))))# food: self.pos.distance_to(food.pos))
		else: closest_food = None

		if len(close_food) == 0:
			"""What the cell does should it be looking for food."""
			#If you can't see food, accelerate in a random direction.
			x = random.uniform(0, World.width)
			y = random.uniform(0, World.height)
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
		distance_to_destination = self.pos.distance_to(self.destination)
		if distance_to_destination > self.distance_to_start_slowing_down():
			self.calc_force()
		
		for f in World.food_at(self.pos, self.radius):
			self.eat(f)

	def update_coords(self):
		"""Updates the cell's position, velocity and acceleration in that order."""
		prev_vel = Vector(self.vel.x, self.vel.y)
		self.pos += self.vel
		if numpy.isnan(self.pos.x):
			self.pos.x = random.uniform(0,World.width)
		if numpy.isnan(self.pos.y):
			self.pos.y = random.uniform(0,World.width)
			
		self.vel += self.acl
		self.acl = self.exerted_force - self.vel*abs(self.vel)*World.resistance*(self.radius)/self.mass
		self.exerted_force = Vector(0.0,0.0)

	def calc_force(self):
		"""Cells calculate how much force they are exerting (prior to resistance)."""
		self.exerted_force = (self.destination - self.pos)*self.walk_force / abs(self.destination - self.pos)
		if self.energy > self.walk_force:
			self.energy -= self.walk_force*1.0
		else:
			self.mass -= self.walk_force*3.0

	def distance_to_start_slowing_down(self):
		"""Calculates the distance from the destination that, once past,
		the cell ought to begin slowing down to reach its destination."""
		return (abs(self.vel) * self.mass) / (World.resistance * self.radius)

	def eat(self, f):
		"""Updates energy and mass according to set emRatio value and removes food item."""
		self.energy += f.energy/self.emRatio
		self.mass += f.energy - (f.energy/self.emRatio)
		World.remove_food(f)
		#The above line automatically resets our task and destination by calling stop_getting_food()

	def weight_management(self):
		"""Updates radius and sight range according to mass and density"""
		self.radius = ( 3.0*self.mass*self.density / (4.0*math.pi) )**(1/2.0)
		self.sight_range = .2 + self.radius
	
	def determine_phenotype(self):
		"""Setting variance for child cell. Called when cell duplicates"""
		self.phenotype.mutate_phenotype() 

	def life_and_death(self):
		"""Checks if cell mass is great enough for division or low enough to cause death.""" 
		"""Brings new cells into existance or removes cell if conditions are true."""
		if self.mass >= self.div_mass and self.energy >= self.div_energy:		
			#Statistics for child cells
			newMass		= self.mass/self.emRatio
			newEnergy	= (self.energy - 3.0)/self.emRatio

			#Create child 1
			x1 = random.uniform(self.pos.x-0.01,self.pos.x+0.01)
			y1 = random.uniform(self.pos.y-0.01,self.pos.y+0.01)
			self.determine_phenotype()
			World.cell_list.append(Cell(x1,y1,newMass,newEnergy,self.vel.x,self.vel.y,self.phenotype))
			
			#Create child 2
			x2 = random.uniform(self.pos.x-0.01,self.pos.x+0.01)
			y2 = random.uniform(self.pos.y-0.01,self.pos.y+0.01)
			self.determine_phenotype()
			World.cell_list.append(Cell(x2,y2,newMass,newEnergy,self.vel.x,self.vel.y,self.phenotype))
						
			#Instantiates children at slightly different positions
			World.remove_cell(self)
		#Kills cell
		elif self.mass <= 0.1:
                        World.kill_cell(self)

        		
	def one_tick(self):
		"""What a cell does every arbitrary unit of time."""
		self.TaskTable[self.task]()
		self.update_coords()
		self.weight_management()
		self.life_and_death()
                
        def collideWith(self, foe):
                """assumed cells are colliding"""
	
	#get distance between cell radii as a vector
		selfPos = self.pos
		foePos = foe.pos
		xDiff = selfPos.x - foePos.x
		yDiff = selfPos.y - foePos.y
		dist = math.sqrt(xDiff**2 + yDiff**2)
                dist += 5
		distVec = Vector(xDiff, yDiff)
		distVec.x = round(distVec.x,3)
		distVec.y = round(distVec.y,3)
		unitVec = distVec/dist
		unitVec.x = round(unitVec.x, 3)
		unitVec.y = round(unitVec.y, 3)

	#make a force vector
		forcApp = 1/dist
		forcApp = round(forcApp, 3)
		forcVec = unitVec * forcApp
		forcVec.x = round(forcVec.x, 3)
		forcVec.y = round(forcVec.y, 3)

	#apply the force vector to other cell
		#the target's acceration is changed
		#by F/target's mass
 		
		targetPushVec = forcVec/foe.mass
		targetPushVec.x = round(targetPushVec.x, 3)
		targetPushVec.y = round(targetPushVec.y, 3)
		foe.acl += -targetPushVec

        def guessedKey(self, vKey):
                vKeyO = vKey % 10 #gets the number in the ones place in vKey
                vKeyT = (vKey - vKeyO)/10 #gets the number in the tens place in vKey
                if self.keyList[vKeyT][vKeyO] == True : #if the cell already knows the key
                        return True
                randN = round(random.random(),2)*100
                randNO = randN % 10
                randNT = (randN - randNO)/10
                #if the guess shares the same tens value and is at least 2 units away from the ones value
                if vKeyT == randNT and vKeyO < randNT + 2 and vKeyO >= randNT - 2:
                        self.keyList[randNT][randNO] = True
                        return True
                return False #if this is reached, all guesses have failed
                
	def randExponent(curve,maximum):
		x=random.randint(0,maximum*100.0)/100.0
		base=(((maximum+curve)/curve))**(1.0/maximum)
		y=curve*(base**x)-curve
		return y
