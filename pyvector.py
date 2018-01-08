import numpy                # I might need this later
import random
import math

class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        print("Vector with coordinates x="+self.x+", y="+self.y+", z="+self.z)
    __repr__ = __str__
    
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
    def random2D():
        theta = random.uniform(0, 2*math.pi)
        x = math.cos(theta)
        y = math.sin(theta)
        return Vector(x, y, 0)
    def random3D():
        base = random2D()
        theta = random.uniform(0, 2*math.pi)
        z = math.sin(theta)
        x = base[0]*math.cos(theta)
        y = base[1]*math.cos(theta)
        return Vector(x, y, z)
    def fromAngle(angle):
        x = math.cos(angle)
        y = math.sin(angle)
        return Vector(x, y, 0)
