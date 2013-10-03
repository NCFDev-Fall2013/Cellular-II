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
