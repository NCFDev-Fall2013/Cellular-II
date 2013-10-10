
import unittest, food, environment, cells, vector, random



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
		print "init_once is a go"

	def test_add_food(self):
		fc=len(global_e.food_set)
		global_e.add_food(10)
		self.assertEquals(len(global_e.food_set), fc+10)
		print "add_food is a go"

#Not yet finished
	def test_add_food_at_location(self):
		global_e.cell_list=[]
		test_cell=cells.Cell(0.1,0.2)
		global_e.cell_list.append(cells.Cell(0.1, 0.2))
		self.assertEquals(global_e.cell_list[0].pos.distance_to(test_cell.pos), 0.0)
		print "add_food_at_location is a go"
	
	
#Tests for Cells
#CellsCreationTest = cells.TestFunctions

#Tests for Food
#FoodTest = food.CreationTest

#Vector Test

class TestVector(unittest.TestCase):
	def setup(self):
		global_e.init_once(10,10)
		#quick fix for global_e use		
		environment = global_e
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



        def setUp(self):
                #import environment
                #environment3 = environment.Environment(10,10)
                max_width = environment3.width 
                max_height = environment3.height
                # set x and y pairs
                #silly rabbit trix are for kids
                x1 = 0
                x2 = 1
                y1 = 0
                y2 = 1
                self.nullVector = vector.Vector(x1,y1)
                self.unitVector = vector.Vector(x2,y2)
                self.v = vector.Vector(.2,.1)
                
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
                #dif(0,0) ==0 ? 
                self.assertEqual(diff(1,1),0)
                self.assertEqual(diff(.5,.3),.2)
                self.assertEqual(diff(.9,.25),.65)

        def test__init__(self):
                newV = Vector(0,1)
                newP = Point(Vector)
                self.assertEqual(newV.y,1)
                self.assertEqual(newV.x,0)

        def test__iadd__(self):
                
                vTemp = v #storing the default in temporary variable vTemp
                v2 = Vector(.3,.2)
                v += v2
                self.assertEqual((v.x,.5))
                self.assertEqual((v.y,.3))
        
                v = vTemp #resetting v to default value, stored in vTemp
                v3 = Vector(0,0)
                v += v3
                self.assertEqual((v.x,.2))
                self.assertEqual((v.x,.1))

                v = vTemp #resetting for further testing 

        def test_add(self):
                self.addResult = unitVector + nullVector
                if not(addResult == unitVector):
                        fail()
                addResult = v + nullVector
                if not(addResult == v):#{}{}{}{}{}{}{}{}{}{}}{}
                        fail()

        def test_sub(self):
                self.subResult = unitVector - nullVector
                if not(addResult == unitVector):
                        fail()
                subResult = v - nullVector
                if not(subResult == v):#{}{}{}{}{}{}{}{}{}{}}{}
                        fail()

        def test_mul(self):
                self.mulResult = unitVector * nullVector
                if not(mulResult == nullVector):
                        fail()
                mulResult = v * unitVector
                if not(mulResult == v):
                        fail()

        def test_div(self):
                self.divResult = v/unitVector
                if not(divResult == v):
                        fail()
                divResult = nullVector/v
                if not(divResult == nullVector):
                       fail()

        def test_neg(self):
                self.negVector = -v
                self.assertEqual(negVector.x, -v.x)
                self.assertEqual(negVector.y, -v.y)
                negVector = -unitVector
                self.assertEqual(negVector.x, -1)
                self.assertEqual(negVector.y, -1)

        def test_abs(self):
                self.assertEqual(abs(unitVector), math.sqrt(2))
                self.assertEqual(abs(nullVector), 0)
                self.assertEqual(round(abs(v),3), 0.224) 

        def test_repr(self):
                vectName = str(unitVector)
                self.assertEqual(vectName, '{1,1)')
                vectName = str(nullVector)
                self.assertEqual(vectName, '(0,0)')
                vectName = str(v)
                self.assertEqual(vectName, '(.2,.1)')

        def test_eq(self):
                testVector = vector.Vector(1,1)
                self.assertEqual(testVector == unitVector, True)
                testVector = vector.Vector(0,0)
                self.assertEqual(testVector == nullVector, True)

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
		self.environmentObj = environment.Environment(10,10)
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

