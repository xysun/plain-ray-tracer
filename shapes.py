'''
different shape classes
* sphere
* triangle
* polygon
'''
from vector import Quadratic, LinearSystem3, Vector3, Matrix3
from vector import THRESHOLD

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
        return hit, closer intersection point
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
            x = q.solve()
            if x > 0:
                return 0, x
            else:
                return -1, None
        else:
            if q.discriminant > 0:
                x = q.solve()
                if x > 0:
                    return 1, x
                else:
                    return -1, None
            elif q.discriminant < 0:
                return -1, None

class Triangle(Shape):
    def __init__(self, a, b, c):
        '''
        a, b, c are 3 vertices of Vector3
        '''
        self.a = a
        self.b = b
        self.c = c
    
    def intersect(self, ray):
        '''
        solve a linear system
        '''
        B = self.a - ray.origin
        A = Matrix3([(self.a - self.b).tolist(),
                     (self.a - self.c).tolist(),
                     ray.direction.tolist()])
        system = LinearSystem3(A, B)
        solution = system.solve()
        if solution is None:
            return -1, None
        beta = solution.x
        gamma = solution.y
        t = solution.z
        alpha = 1 - beta - gamma

        if t < 0:
            return -1, None
        else:
            # edge: if ray is parallel to either a,b,c
            # TODO: how to detect edge with threshold band
            r = ray.origin + ray.direction.scale(t)
            if r.is_parallel(self.a) or r.is_parallel(self.b) or r.is_parallel(self.c):
                return 0, t
            # inner, everyone > 0
            if alpha > 0 and beta > 0 and gamma > 0:
                return 1, t
        # catch-all case
        return -1, None

class Polygon(Shape):
    def __init__(self, vertices):
        '''
        vertices: Vector3 list, specified in counterclockwise manner
        '''
        pass
