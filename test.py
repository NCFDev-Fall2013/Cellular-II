import food, cells, random
import unittest
class TestFood(unittest.TestCase):
	def setUp(self):
		self.x=1.3
		self.y=5.7
		self.foodObj = food.Food(self.x,self.y)
		
	def test_foodStats(self):
		self.assertEqual(self.foodObj.energy, 0.5)
		self.assertTrue(self.foodObj.pos.x, self.x%1)
		self.assertTrue(self.foodObj.pos.y, self.y%1)



if __name__ == '__main__':
    unittest.main()
