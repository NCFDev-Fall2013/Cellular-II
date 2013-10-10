import unittest, food, environment, cells, vector

#Tests for Environment
#EnvironmentCreationTest = environment.CreationTest

#Global Environment that can be accessed by all tests
global_e=environment.Environment(10,10)
#THERE CAN ONLY BE ONE environment 


class TestEnvironment(unittest.TestCase):
	#Initilization

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
		print "Add food is a go"

#Not yet finished
"""
	def test_add_food_at_location(self):
		global_e.cell_list=[]
		test_cell=cells.Cell(0.1,0.2)
		global_e.cell_list.append(cells.Cell(0.1, 0.2))
		self.assertTrue(global_e.cell_list[0].pos == Point(0.1,0.2))
"""		
	
#Tests for Cells
#CellsCreationTest = cells.TestFunctions

#Tests for Food
#FoodTest = food.CreationTest

#Vector Test
class TestVector(unittest.TestCase):
	def setup(self):
		import environment
		environment = environment.Environment(10,10)
		max_width = environment.width 
		max_height = environment.height
		# set x and y pairs
		

	def test_distance(self):
		# test if distance(testpoints= known distance
		self.assertEqual(round(distance(0,0,.9,.9),3),1.273)
		self.assertEqual(distance(.9,.9,0,0),0)
		self.assertEqual(distance(.5,.3,.2,.7),.5)
		self.assertEqual(round((distance(.4,.3,.2,.7),5)),.44721)
		self.assertEqual(distance(.3,.2,.3,.2),0)
		self.assert_false(distance(0,0,self.width,self.height) == math.sqrt(2))

		
	def test_diff(self):
		# test if diff(testpoints= known distance
		self.assertEqual(diff(0,0),0)
		dif(0,0) ==0 ? 
		self.assertEqual(diff(1,1),0)
		self.assertEqual(diff(.5,.3).2)
		self.assertEqual(diff(.9,.25),.65)

	def test__init__(self):
		v = Vector(0,1)
		self.assertEqual(v.y,1)
		self.assertEqual(v.x,0)

	def test__iadd__(self):
		v = Vector(.2,.1)
		v2 = Vector(.3,.2)
		self.assertEqual((v.__iadd__(v2).x,.5))
		self.assertEqual((v.__iadd__(v2).y,.3))

		v3 = Vector(0,0)
		self.assertEqual((v.__iadd__(v3).x,.2))
		self.assertEqual((v.__iadd__(v3).x,.1))

if __name__ == "__main__":
	#environment.Environment(10, 10)
	#environment.Environment(10, 10) #this should fail
	unittest.main()



