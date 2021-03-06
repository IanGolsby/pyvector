#   PyVector is a Python module to handle vector math in 2 and 3 dimensions.

import numpy, random, math

class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        print("Vector with coordinates x="+self.x+", y="+self.y+", z="+self.z)
    __repr__ = __str__
    
    # Assign custom values to a vector
    def assign(self, x, y=None, z=None):
        if type(y) is None and type(z) is None:
            if type(x) is Vector:
                self.x = x.x
                self.y = x.y
                self.z = x.z
            else:
                raise TypeError("With only one parameter, this function expects a Vector")
        elif type(z) is None:
            if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float):
                self.x = x
                self.y = y
            else:
                raise TypeError("Expected two numerical values")
        else:
            if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float) and (type(z) is int or type(z) is float):
                self.x = x
                self.y = y
                self.z = z
        return self
    
    # Returns a unit vector with random coordinates in two dimensions (z=0)
    def random2D(self):
        theta = random.uniform(0, 2*math.pi)
        x = math.cos(theta)
        y = math.sin(theta)
        return Vector(x, y, 0)
   
    # Returns a unit vector with random coordinates in three dimensions
    def random3D(self):
        base = random2D()
        theta = random.uniform(0, 2*math.pi)
        z = math.sin(theta)
        x = base[0]*math.cos(theta)
        y = base[1]*math.cos(theta)
        return Vector(x, y, z)
    
    # Returns a unit vector at a specified angle in radians
    def fromAngle(self, angle):
        x = math.cos(angle)
        y = math.sin(angle)
        return Vector(x, y, 0)

    # Returns a list containing the x y z values of a Vector
    def list(self):
        return [self.x, self.y, self.z]
    
    # Returns the magnitude of a vector
    def mag(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    # Returns the square of the magnitude of a vector
    def magSq(self):
        return self.x*self.x+self.y*self.y+self.z*self.z
    
    # Adds things
    def add(self, x, y=None, z=None):
        if type(y) is None and type(z) is None:
            if type(x) is Vector:
                self.x+=x.x
                self.y+=x.y
                self.z+=x.z
            else:
                raise TypeError("Expected single Vector")
        elif type(z) is None:
            if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float):
                self.x+=x
                self.y+=y
            else:
                raise TypeError("Expected two numerical inputs")
        else:
            if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float) and (type(z) is int or type(z) is float):
                self.x+=x
                self.y+=y
                self.z+=z
            else:
                raise TypeError("Expected three numerical inputs")
        return Vector(self.x, self.y, self.z)
    
    # Subtracts things
    def sub(self, x, y=None, z=None):
        if type(y) is None and type(z) is None:
            if type(x) is Vector:
                self.x-=x.x
                self.y-=x.y
                self.z-=x.z
            else:
                raise TypeError("Expected single Vector")
        elif type(z) is None:
            if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float):
                self.x-=x
                self.y-=y
            else:
                raise TypeError("Expected two numerical inputs")
        else:
            if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float) and (type(z) is int or type(z) is float):
                self.x-=x
                self.y-=y
                self.z-=z
            else:
                raise TypeError("Expected three numerical inputs")
        return Vector(self.x, self.y, self.z)
    
    # Multiplies vector by a scalar
    def mult(self, scalar):
        self.x*=scalar
        self.y*=scalar
        self.z*=scalar
        return Vector(self.x, self.y, self.z)
    
    # Divides vector by a scalar
    def div(self, scalar):
        self.x/=scalar
        self.y/=scalar
        self.z/=scalar
        return Vector(self.x, self.y, self.z)
   
    # Calculates distance between two vectors
    def dist(self, v):
        if type(v) is Vector:
            return math.sqrt((self.x-v.x**2)+(self.y-v.y**2)+(self.z-v.z**2))
        else:
            raise TypeError("Expected vector, got "+type(v))
    
    # Returns list representation of a vector
    def array(self):
        return [self.x, self.y, self.z]

    # Calculates dot product of two vectors or a vector and 3 components
    def dot(self, x, y=None, z=None):
        if type(x) is Vector:
            return self.x*x.x + self.y*x.y + self.z*x.z
        elif (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float) and (type(z) is int or type(z) is float):
            return self.x*x + self.y*y + self.z*z
        else:
            raise TypeError("")
    
    # Calculates the dot product of two vectors
    def cross(self, v):
        return Vector(self.y*v.z-v.y*self.z, self.z*v*x-v.z*self.x, self.x*v.y-v.x*self.y)
    
    # Normalizes vector to a magnitude of one
    def normalize(self):
		m = self.mag()
		self.div(m)
		return self
	
	# Changes vector to have a specified magnitude
	def setMag(self, m):
		mr = m/self.mag()
		self.mult(mr)
		return self
	
	# Limits vector to a specified magnitude
	def limit(self, m):
		if self.mag() > m:
			return self.setMag(m)
		else:
			return self
	
	# Returns angle in radians that the Vector is pointing
	def heading(self):
		return math.atan2(self.y, self.x)
	
	# Rotates a 2D vector by an angle
	def rotate(self, angle):
		temp = self.x
		x = self.x*math.cos(angle)-self.y*math.sin(angle)
		y = temp*math.sin(angle)+self.y*math.cos(angle)
		return self
