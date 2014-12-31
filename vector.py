'''
linear algebra utilities
'''
import math

THRESHOLD = 0.1

class Quadratic(object):
    '''
    quadratic function: Ax2 + BX + C = 0
    '''
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.discriminant = B * B - 4 * A * C

class Vector3(object):
    '''
    vector in orthogonal unit basis vectors
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.length = math.sqrt(x*x + y*y + z*z)
    
    def __str__(self):
        return ','.join([str(self.x), str(self.y), str(self.z)])
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Vector3(x,y,z)
    
    def scale(self, scalar):
        x = scalar * self.x
        y = scalar * self.y
        z = scalar * self.z

        return Vector3(x,y,z)
    
    def cross_product(self, other):
        '''
        dot product of self x other
        return a Vector3
        '''
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x

        return Vector3(x,y,z)
    
    def normalize(self):
        '''
        normalize to unit-length vector
        '''
        return Vector3(self.x / self.length,
                       self.y / self.length,
                       self.z / self.length)
