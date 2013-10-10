import unittest, food, environment, cells, os
from vector import Point
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

	def test_add_food_at_location(self):
		global_e.cell_list=[]
		test_cell=cells.Cell(0.1,0.2)
		global_e.cell_list.append(cells.Cell(0.1, 0.2))
		self.assertTrue(global_e.cell_list[0].pos == Point(0.1,0.2))
		
	
#Tests for Cells
#CellsCreationTest = cells.TestFunctions

#Tests for Food
#FoodTest = food.CreationTest

if __name__ == "__main__":
	#environment.Environment(10, 10)
	#environment.Environment(10, 10) #this should fail
	unittest.main()
