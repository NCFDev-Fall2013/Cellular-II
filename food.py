#=====Custom Modules=====#
from vector import Point

class Food:
	def __init__(self, x, y):
		self.energy = 0.5
		self.pos = Point(x,y)
		self.pos.fit_to_torus()
        
