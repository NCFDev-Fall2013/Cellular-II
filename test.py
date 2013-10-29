import unittest, food, environment, cells, vector, random, math

#Tests for Environment
#EnvironmentCreationTest = environment.CreationTest

#Global Environment that can be accessed by all tests
global_e=environment.Environment(10,10)
#THERE CAN ONLY BE ONE environment 
global_Vecsx1 = 0
global_Vecsx2 = 1
global_Vecsy1 = 0
global_Vecsy2 = 1
global_VecsnullVector = vector.Vector(global_Vecsx1,global_Vecsy1)
global_VecsunitVector = vector.Vector(global_Vecsx2,global_Vecsy2)
global_Vecsv = vector.Vector(.2,.1)

class TestEnvironment(unittest.TestCase):
	def setUp(self):
		#Resets Test Environment global_e
		global_e.init_once(10,10)     
	
	def test_init_once(self):
		global_e.init_once(10,10)       
		self.assertTrue(global_e.cell_list)
		self.assertEquals(global_e.width, global_e.height,1.0)
		self.assertEquals(global_e.turn, 0)
		self.assertEquals(global_e.reseed_prob,10)
		self.assertEquals(global_e.resistance, 600)
		self.assertEquals(len(global_e.food_set), 10)

	def test_add_food(self):
		fc=len(global_e.food_set)
		global_e.add_food(10)
		self.assertEquals(len(global_e.food_set), fc+10)

	def test_add_food_at_location(self):
		global_e.cell_list=[]
		test_cell=cells.Cell(0.1,0.2)
		global_e.cell_list.append(cells.Cell(0.1, 0.2))
		self.assertEquals(global_e.cell_list[0].pos.distance_to(test_cell.pos), 0.0)
	
	def test_add_cells(self):
		global_e.cell_list=[]
		global_e.add_cells(5)
		self.assertEquals(len(global_e.cell_list),5)

	def test_add_cells_at_location(self):
		pass

	def test_tick(self):
		pass

	def test_food_at(self):
		pass

	def test_remove_food(self):
		pass

	def test_remove_cell(self):
		pass

	def test_kill_cell(self): 
		pass

	def test_print_table(self):
		pass

#Tests for Cells
#CellsCreationTest = cells.TestFunctions

#Tests for Food
#FoodTest = food.CreationTest

#Vector Test

class TestVector(unittest.TestCase):
#Needs to be fixed
	"""
	def test__iadd__(self):
		print "In the garden of eden",global_VecsunitVector
		#Invalid variable global_Vescsv                
		print "test_iadd which involves 0",global_Vecsv 
		vTemp = global_Vecsv #storing the default in temporary variable vTemp
		v2 = Vector(.3,.2)
		global_Vecsv += v2
		self.assertEqual((global_Vecsv.x,.5))
		self.assertEqual((global_Vecsv.y,.3))
		print "test_iadd which involves 1",global_Vecsv
	
		global_Vecsv = vTemp #resetting v to default value, stored in vTemp
		v3 = Vector(0,0)
		global_Vecsv += v3
		self.assertEqual((global_Vecsv.x,.2))
		self.assertEqual((global_Vecsv.x,.1))
		global_Vecsv = vTemp
		print "test_iadd which involves 2",global_Vecsv
	"""

	def setUp(self):
		global_e.init_once(10,10)
		environment = global_e
		#import environment
		#environment3 = environment.Environment(10,10)
		max_width = environment.width 
		max_height = environment.height
		# set x and y pairs
		#silly rabbit trix are for kids
		global_Vecsx1 = 0
		global_Vecsx2 = 1
		global_Vecsy1 = 0
		global_Vecsy2 = 1
		global_VecsnullVector = vector.Vector(global_Vecsx1,global_Vecsy1)
		global_VecsunitVector = vector.Vector(global_Vecsx2,global_Vecsy2)
		global_Vecsv = vector.Vector(.2,.1)
		
	def test_distance(self):
		# test if distance(testpoints= known distance
		self.assertEqual(round(vector.distance(0.0,0.0,0.9,0.9),3),1.273)
		self.assertEqual(round(vector.distance(0.9,0.9,0.0,0.0),3),1.273)
		self.assertEqual(round(vector.distance(0.5,0.3,0.2,0.7),3),0.5)
		self.assertEqual(round(vector.distance(0.4,0.3,0.2,0.7),3),0.447)
		self.assertEqual(vector.distance(.3,.2,.3,.2),0)
		#The below test was taken out until it can be revised. Test_Vector has no attribute width or height.                 
#		self.assertFalse(vector.distance(0,0,self.width,self.height) == math.sqrt(2))

		
	def test_diff(self):
		# test if diff(testpoints= known distance
		self.assertEqual(vector.diff(0,0),0)
		#dif(0,0) ==0 ? 
		self.assertEqual(vector.diff(1,1),0)
		self.assertEqual(round(vector.diff(.5,.3),3),.2)
		self.assertEqual(round(vector.diff(.9,.25),3),-0.35)

	def test__init__(self):
		newV = vector.Vector(0,1)
	       # newP = vector.Point(self,newV)
		self.assertEqual(newV.y,1)
		self.assertEqual(newV.x,0)

	def test_add(self):
		addResult = global_VecsunitVector + global_VecsnullVector
		if not(addResult == global_VecsunitVector):
			fail()
		addResult = global_Vecsv + global_VecsnullVector
		if not(addResult == global_Vecsv):#{}{}{}{}{}{}{}{}{}{}}{}
			fail()

	def test_sub(self):
		subResult = global_VecsunitVector - global_VecsnullVector
		if not(subResult == global_VecsunitVector):
			fail()
		subResult = global_Vecsv - global_VecsnullVector
		if not(subResult == global_Vecsv):#{}{}{}{}{}{}{}{}{}{}}{}
			fail()

	def test_mul(self):
		mulResult = global_VecsunitVector * global_VecsnullVector
		if not(mulResult == 0):
			fail()
		mulResult = global_Vecsv * global_VecsunitVector
		if not(mulResult == global_Vecsv.x + global_Vecsv.y):
			fail()

	def test_div(self):
		divResult = global_Vecsv/global_VecsunitVector
		if not(divResult == global_Vecsv):
			fail()
		divResult = global_VecsnullVector/global_Vecsv
		if not(divResult == global_VecsnullVector):
		       fail()

	def test_neg(self):
		negVector = -global_Vecsv
		self.assertEqual(negVector.x, -global_Vecsv.x)
		self.assertEqual(negVector.y, -global_Vecsv.y)
		negVector = -global_VecsunitVector
		self.assertEqual(negVector.x, -1)
		self.assertEqual(negVector.y, -1)

	def test_abs(self):
		self.assertEqual(abs(global_VecsunitVector), math.sqrt(2))
		self.assertEqual(abs(global_VecsnullVector), 0)
		self.assertEqual(round(abs(global_Vecsv),3), 0.224) 

	def test_repr(self):
		vectName = str(global_VecsunitVector)
		self.assertEqual(vectName, '(1,1)')
		vectName = str(global_VecsnullVector)
		self.assertEqual(vectName, '(0,0)')
		vectName = str(global_Vecsv)
		self.assertEqual(vectName, '(0.2,0.1)')

	def test_eq(self):
		testVector = vector.Vector(1,1)
		self.assertEqual(testVector == global_VecsunitVector, True)
		testVector = vector.Vector(0,0)
		self.assertEqual(testVector == global_VecsnullVector, True)

##        def test_fit_to_torus(self):
##                if not (self.x>=0 and self.x<1):
##                        fail()
##                if not (self.y>=0 and self.y<1):
##                        fail()      
		


class TestFood(unittest.TestCase):
	def setUp(self):
		self.x=1.3
		self.y=5.7
		self.foodObj = food.Food(self.x,self.y)

	def test_foodStats(self):
		self.assertEqual(self.foodObj.energy, 0.5)
		self.assertEqual(self.foodObj.pos.x, self.x%1)
		self.assertEqual(self.foodObj.pos.y, self.y%1)


class TestCells(unittest.TestCase):
	def setUp(self):
		self.environmentObj = global_e
		self.cellList = self.environmentObj.cell_list
		
	def test_init(self):
		pheno = [2.0,.001,.5,.6,.005,None,0]
		
		Alfred = cells.Cell(.1,.9,.11,7)
		Bob = cells.Cell(.5,.5)
		Cathy = cells.Cell(.13,.37,x_vel= .4,y_vel= -.4)
		Dingus = cells.Cell(.1,.1, .1,.1, .1,.1, ["A","B","C","D",1.0,"F","G"])
		
		self.assertEqual(Bob.pos.x , .5)
		self.assertEqual(Bob.pos.y , .5)
		self.assertEqual(Bob.vel.x , 0)
		self.assertEqual(Bob.vel.y , 0)
		self.assertEqual(Bob.acl.x , 0)
		self.assertEqual(Bob.acl.y , 0)
		# self.assertEqual(Bob.phenotype , pheno)
		self.assertEqual(Bob.emRatio, pheno[0])
		self.assertEqual(Bob.walk_force, pheno[1])
		self.assertEqual(Bob.div_energy, pheno[2])
		self.assertEqual(Bob.div_mass, pheno[3])
		self.assertEqual(Bob.density, pheno[4])
		# self.assertEqual(Bob.color, pheno[5])
		self.assertEqual(Bob.mutation_chance, pheno[6])
		self.assertEqual(Bob.energy, .1)
		self.assertEqual(Bob.mass, .3)
		# self.assertEqual(Bob.exerted_force, Vector(0.0,0.0))
		self.assertEqual(Bob.task, None)
		self.assertEqual(Bob.destination, None)
		self.assertEqual(Bob.destination_type, None)
		self.assertEqual(Bob.TaskTable[None], Bob.task_none)
		self.assertEqual(Bob.TaskTable["FindingFood"], Bob.task_finding_food)
		self.assertEqual(Bob.TaskTable["GettingFood"], Bob.task_getting_food)
		self.assertEqual(Alfred.pos.x , .1)
		self.assertEqual(Alfred.pos.y , .9)
		self.assertEqual(Alfred.mass , .11)
		self.assertEqual(Alfred.energy , 7)
		self.assertEqual(Cathy.pos.x , .13)
		self.assertEqual(Cathy.pos.y , .37)
		self.assertEqual(Cathy.mass , .3)
		self.assertEqual(Cathy.energy , .1)
		self.assertEqual(Cathy.vel.x , .4)
		self.assertEqual(Cathy.vel.y , -.4)
		self.assertEqual(Dingus.pos.x , .1)
		self.assertEqual(Dingus.pos.y , .1)
		self.assertEqual(Dingus.mass , .1)
		self.assertEqual(Dingus.energy , .1)
		self.assertEqual(Dingus.vel.x , .1)
		self.assertEqual(Dingus.vel.y , .1)
		self.assertEqual(Dingus.phenotype , ["A","B","C","D",1.0,"F","G"])
		self.assertEqual(Dingus.emRatio , "A")
		self.assertEqual(Dingus.walk_force , "B")
		self.assertEqual(Dingus.div_energy , "C")
		self.assertEqual(Dingus.div_mass , "D")
		self.assertEqual(Dingus.density , 1.0)
		self.assertEqual(Dingus.color , "F")
		self.assertEqual(Dingus.mutation_chance , "G")
		
	def test_task_none(self):
		Alph = cells.Cell(0,0)
		self.assertEqual(Alph.task , None)
		Alph.task_none()
		self.assertEqual(Alph.task , "FindingFood")
		Alph.task = None
		Alph.TaskTable[Alph.task]()
		self.assertEqual(Alph.task , "FindingFood")

	def test_task_finding_food_fail(self):
		"""Testing that a cell will be looking for food"""
		global_e.cell_list = []
		global_e.food_set  = set()
		Alph = cells.Cell(.5,.5)
		Alph.task = "FindingFood"
		self.assertEqual(Alph.destination , None)
		self.assertEqual(Alph.destination_type , None)
		Alph.TaskTable[Alph.task]()
		self.assertEqual(Alph.destination_type , "Exploration")
		Alph.one_tick()
		self.assertEqual(Alph.destination_type , "Exploration")

	def test_task_finding_food_success(self):
		"""Testing that a cell should be able to find food"""
		global_e.cell_list = []
		global_e.food_set  = set()
		global_e.add_cell_at_location(vector.Point(.5,.5))
		Steve = global_e.cell_list[0]
		global_e.tick()
		global_e.tick()
		invisible = vector.Point(Steve.pos.x + Steve.sight_range + .1 , Steve.pos.y + Steve.sight_range + .1)
		visible   = vector.Point(Steve.pos.x + Steve.sight_range - .1 , Steve.pos.y + Steve.sight_range - .1)
		# Confirm Steve does not find the "invisible" food
		global_e.add_food_at_location(invisible)
		self.assertEqual(Steve.task , "FindingFood")
		self.assertEqual(Steve.destination_type , "Exploration")
		global_e.tick()
		self.assertEqual(Steve.task , "FindingFood")
		self.assertEqual(Steve.destination_type , "Exploration")
		# Confirm Steve does find the "visible" food
		global_e.add_food_at_location(visible)
		global_e.tick()
		self.assertEqual(Steve.task , "GettingFood")
		self.assertEqual(Steve.destination_type , "Food")
		self.assertEqual(Steve.destination.x , visible.x)
		self.assertEqual(Steve.destination.y, visible.y)
		
	def test_life_and_death(self):
	#uncomment print statements to see live output
		babies = 0
		corpses = 0
		duplicate = list(self.cellList)
		for cell in duplicate:
			cell.div_mass = .3
			cell.div_energy = .3
			cell.emRation = 2
			cell.mass = round(random.uniform(.0,.5),2)
			cell.energy = round(random.uniform(.0,.5),2)
			orig = len(self.cellList)
			cell.life_and_death()
			if cell.mass>= cell.div_mass and cell.energy >= cell.div_energy:
				self.assertEqual(len(self.cellList),(orig+1))
				corpses+=1
				babies+=2
				#print "A cell of mass",cell.mass,"has been sacrificed to the fertility gods.\n"
			elif cell.mass <= 0.1:
				self.assertEqual(len(self.cellList),(orig-1))
				corpses+=1
				#print "A cell of mass",cell.mass,"has died of starvation.\n"
			else:
				self.assertEqual(len(self.cellList),(orig))
				#print "A cell of mass",cell.mass,"has lived to fight another day.\n"
		#print "\n",babies,"new cells were made and",corpses,"cells died."
		#print len(self.cellList),"cells remain."
	
if __name__ == '__main__':
	unittest.main()

