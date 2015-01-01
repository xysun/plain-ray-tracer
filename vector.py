'''
math & linear algebra utilities
'''
import math

THRESHOLD = 0.1

class Matrix3(object):
    '''
    3x3 matrix
    '''
    def __init__(self, columns):
        '''
        columns: [[1st_column], [2nd_column], [3rd_column]]
        eg: for matrix
                      [1,2,3
                       4,5,6
                       7,8,9]
            columns = [[1,4,7], [2,5,8], [3,6,9]]
        '''
        self.columns = columns

    def determinant(self):
        '''calculate determinant'''
        a,d,g = self.columns[0]
        b,e,h = self.columns[1]
        c,f,i = self.columns[2]
        
        return a * (e*i - f*h) - b * (d*i - f*g) + c * (d*h - e*g)

class LinearSystem3(object):
    '''
    a dimension3 linear system of Ax = B, i.e. Matrix3 x Vector3 = Vector3
    '''
    def __init__(self, A, B):
        '''
        A: Matrix3
        B: Vector3
        '''
        self.A = A
        self.B = [B.x, B.y, B.z]
    
    def solve(self):
        '''
        solve for x of Vector3 using cramer's rule
        ''' 
        # TODO: what if dx = 0? 
        D = self.A
        Dx = Matrix3([self.B, self.A.columns[1], self.A.columns[2]])
        Dy = Matrix3([self.A.columns[0], self.B, self.A.columns[2]])
        Dz = Matrix3([self.A.columns[0], self.A.columns[1], self.B])
        
        d = D.determinant()
        dx = Dx.determinant()
        dy = Dy.determinant()
        dz = Dz.determinant()

        return Vector3(dx / float(d), dy / float(d), dz / float(d))


class Quadratic(object):
    '''
    quadratic function: Ax2 + BX + C = 0
    '''
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.discriminant = B * B - 4 * A * C
    
    def solve(self):
        if abs(self.discriminant) <= THRESHOLD:
            # 1 solution
            return -self.B / (2*self.A)
        else:
            if self.discriminant < 0:
                return None
            else: # 2 solutions, return smaller
                return -self.B - math.sqrt(self.discriminant) / (2 * self.A)

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
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vector3(x,y,z)
    
    def tolist(self):
        return [self.x, self.y, self.z]
    
    def scale(self, scalar):
        x = scalar * self.x
        y = scalar * self.y
        z = scalar * self.z

        return Vector3(x,y,z)
    
    def dot_product(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z

        return x + y + z
    
    def is_parallel(self, other):
        '''
        two vectors are parallel if a * b = |a| * |b|
        '''
        dot_product = self.dot_product(other)
        len_product = self.length * other.length

        return abs(dot_product) == len_product

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
