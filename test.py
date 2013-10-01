import food, cells, unittest
class TestFood(unittest.TestCase):
	def setUp(self):
		self.foodObj = food.Food(1,5)
		
	def foodStats(self):
		self.assertEquals(self.foodObj.energy, 0.5)
		self.assertEquals(self.foodObj.x, 1)
		self.assertEquals(self.foodObj.y, 5)

unittest.main()
