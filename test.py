import food, cells, environment, vector, random
import unittest


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
		self.x = .54
		self.y = .45
		self.environmentObj = environment.Environment(9,9)
		self.environmentObj.add_cell_at_location(vector.Point(self.x,self.y))
		self.cellList = self.environmentObj.cell_list
		
		
	def test_life_and_death(self):
		babies = 0
		corpses = 0
		for cell in self.cellList:
			cell.div_mass = .3
			cell.div_energy = .3
			cell.mass = round(random.uniform(.0,.5),2)
			cell.energy = round(random.uniform(.0,.5),2)
			orig = len(self.cellList)
			cell.life_and_death()
			if cell.mass>= cell.div_mass and cell.energy >= cell.div_energy:
				self.assertEqual(len(self.cellList),(orig+1))
				corpses+=1
				babies+=2
				print "Asexual is best sexual"
			elif cell.mass <= 0.1:
				self.assertEqual(len(self.cellList),(orig-1))
				corpses+=1
				print cell,"has died."
			else:
				self.assertEqual(len(self.cellList),(orig))
				print "nothing happened."
		print "\n",babies,"babies were made."
		print "and",corpses,"cells died."
		print len(self.cellList),"cells remain."
		if babies == 0:
			print "\nno babies were made to test, generating again..."
			self.test_life_and_death()
	
if __name__ == '__main__':
    unittest.main()
