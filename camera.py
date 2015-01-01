'''
camera class
'''

from tracer import Ray

class Camera(object):
    def __init__(self, e, w, up):
        '''
        e: eye_point, Vector3
        w: opposite to view direction, Vector3
        up: up direction, Vector3
        '''
        self.e = e
        self.w = w
        self.up = up

        self.build_basis()
    
    def build_basis(self):
        '''
        build u, v, w from e, w, up
        u, v, w will be orthonormal
        Reference: Fundamentals of Computer Graphics, 2.4.7
        
        '''
        # w: normalize to unit vector
        self.w = self.w.normalize()
        
        # u: w x up, normalized
        u = self.up.cross_product(self.w)
        self.u = u.normalize()

        # v: 
        self.v = self.w.cross_product(self.u)

    def set_size(self, l, r, b, t):
        '''
        set left, right, bottom, top, centered at self.e
        l < 0 < r
        b < 0 < t
        '''
        self.l = l
        self.r = r
        self.b = b
        self.t = t
    
    def compute_ray(self, i, j, nx, ny):
        pass

class ParallelCamera(Camera):
    def compute_ray(self, i, j, nx, ny):
        '''
        get the ray at (i,j) position
        start at topleft, following Pillow's convention
        '''
        u = self.l + (self.r - self.l) / float(nx) * (i + 0.5)
        v = self.t - (self.t - self.b) / float(ny) * (j + 0.5)
        direction = self.w.scale(-1)
        origin = self.e + self.u.scale(u) + self.v.scale(v)
        
        return Ray(origin, direction)
