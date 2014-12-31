'''
different shape classes
* sphere
* triangle
* polygon
'''
from vector import Quadratic, THRESHOLD

class Shape(object):
    '''
    parent class for all shapes
    '''
    def __init__(self):
        pass

    def set_color(self, edge_color, in_color):
        '''
        color are in (R,G,B) tuples
        '''
        self.edge_color = edge_color
        self.in_color = in_color
   
    def intersect(self, ray):
        '''
        check if will intersect by ray
        return hit
        hit: 1 -> inside, 0 -> on edge, -1 -> not hit
        '''
        pass

class Sphere(Shape):
    def __init__(self, origin, radius):
        '''
        origin: Vector3
        radius: float
        '''
        self.origin = origin
        self.radius = radius
    
    def intersect(self, ray):
        e = ray.origin
        d = ray.direction
        c = self.origin
        r = self.radius
        
        A = d.x**2 + d.y**2 + d.z**2
        B = 2 * (e.x*d.x - d.x*c.x + e.y*d.y - d.y*c.y + e.z*d.z - d.z*c.z)
        C = (e.x - c.x)**2 + (e.y - c.y)**2 + (e.z - c.z)**2 - r**2

        q = Quadratic(A, B, C)

        if abs(q.discriminant) <= THRESHOLD:
            return 0
        else:
            if q.discriminant > 0:
                return 1
            elif q.discriminant < 0:
                return -1

class Triangle(Shape):
    pass

class Polygon(Shape):
    def __init__(self, vertices):
        '''
        vertices: Vector3 list, specified in counterclockwise manner
        '''
        pass
