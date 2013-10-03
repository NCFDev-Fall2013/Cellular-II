import vector
from cells import Cell

class Food:
	def __init__(self, x, y):
		self.energy = 0.5
		self.pos = vector.Point(x, y)
