from math import sqrt
from math import fabs
from math import fmod
import environment
#assert(environment.Environment().width == 1 and environment.Environment().height == 1, #"vector.py assumes world is 1x1")

	
def distance(x1, y1, x2, y2):
	"""Calculates and returns the distance""" 
	xdiff = fabs(x1 - x2)
	ydiff = fabs(y1 - y2)
	if(xdiff < (1.0 - xdiff)):
                xdiff = xdiff
        else:
		xdiff= (1.0 - xdiff)	
	if( ydiff < (1.0 - ydiff)):
                ydiff = ydiff
        else:
		ydiff = (1.0 - ydiff)
	return sqrt(xdiff*xdiff + ydiff*ydiff)

def diff(a, b):
	"""Helps vectors calculate the difference."""
	return fmod(a - b + 1.5, 1.0) - 0.5 # < -0.5 and > 0.5 wrap around using fmod

class Vector(object):
	__slots__ = ('x', 'y')
	"""Vector in toroidal space defined by the dimensions of Environment()."""
	def __init__(self, x, y):
		"""Instantiates the two values for the vector."""
		self.x = x
		self.y = y
	def __iadd__(self, other):
		"""Increase vector."""
		self.x = self.x + other.x
		self.y = self.y + other.y
		return self
	def __add__(self, other):
		"""Sum of vectors."""
		return Vector(self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		"""Return simple difference of vectors."""
		return Vector(self.x - other.x, self.y - other.y)
	def __mul__(self, other):
		"""Multiplication of vectors."""
		if type(other) == type(self):
			return self.x*other.x + self.y*other.y
		elif type(other) == int or type(other) == float:
			return Vector(self.x*other, self.y*other)
	def __div__(self, other):
		"""Division of vectors."""
		if type(other) == type(self):
			return Vector(self.x/other.x, self.y/other.y)
		elif type(other) == int or type(other) == float:
			return Vector(self.x/other, self.y/other)
	def __neg__(self):
		"""Makes the vector negative."""
		return Vector(-self.x, -self.y)
	def __abs__(self):
		"""Magnitude of the vector."""
		return (self.x**2 + self.y**2)**0.5
	def __repr__(self):
		"""Presents the representation of the vector."""
		return '(' + str(self.x) + ',' + str(self.y) + ')'

class Point(Vector):
	def fit_to_torus(self):
		"""Check vector."""
#		self.x %= 1
#		self.y %= 1
		self.x %= environment.Environment().width
		self.y %= environment.Environment().height
	def __init__(self, x, y):
		"""Instantiates the two values for the vector."""
		super(Point, self).__init__(x, y)
	def __iadd__(self, other):
		"""Increases the point vector"""
		super(Point, self).__iadd__(other)
		self.fit_to_torus()
		return self
	def __add__(self, other):
		"""Adds a point vector to another"""
		result = super(Point, self).__add__(other)
		result.fit_to_torus()
		return result
	def __sub__(self, other):
		"""Return shortest difference vector pointing from other to self."""
		return Vector(diff(self.x, other.x), diff(self.y, other.y))
	def distance_to(self, other):
		"""Has no meaning for vectors"""
		return distance(self.x, self.y, other.x, other.y)
		

class VectorAroundZero(object):
	"""Vector in toroidal space (x,y) with -0.5 <= x,y <= 0.5
	I think this is cleaner. Might be an argument for having a [-0.5, 0.5] coordinate system.
	Adapting the program to use this would be some work though."""
	__slots__ = ('_x', '_y')
	def __init__(self, x, y): self.x = x; self.y = y
	def __repr__(self): return '(' + str(self._x) + ',' + str(self._y) + ')'
	def __add__(self, other): return VectorAroundZero(self._x + other._x, self._y + other._y)
	def __sub__(self, other): return self + -other
	def __neg__(self): return VectorAroundZero(-self._x, -self._y)
	def __abs__(self): return (self._x**2 + self._y**2)**0.5
	def distance_to(self, other): return abs(self - other)
	@property
	def x(self   ): return self._x
	@x.setter
	def x(self, x): self._x = ((x + 0.5) % 1) - 0.5
	@property
	def y(self   ): return self._y
	@y.setter
	def y(self, y): self._y = ((y + 0.5) % 1) - 0.5
