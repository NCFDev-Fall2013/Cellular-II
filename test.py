import unittest, food, environment, cells, vector

if __name__ == "__main__":
	environment.Environment(10, 10)
	#environment.Environment(10, 10) #this should fail
	unittest.main()

class TestVector(unittest.TestCase):
	def setup(self):
		import environment
		environment = environment.Environment(10,10)
		max_width = environment.width 
		max_height = environment.height
		# set x and y pairs
		#silly rabbit trix are for kids
                x1 = 0
                x2 = 1
                y1 = 0
                y2 = 1
                self.nullVector = vector.Vector(x1,y1)
                self.unitVector = vector.Vector(x2,y2)
                        

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

        def test_add(self):
            #pretty much the same as iadd

        def test_sub(self):
            self.subTester = (unitVector - nullVector)
            self.assertEqual((unitVector - nullVector), s
