'''
samples of how to piece everything together
'''
from camera import ParallelCamera
from shapes import Sphere
from tracer import Tracer
from vector import Vector3

# factories of shapes

# sphere with white edge and green inside
origin = Vector3(2, 0, 2)
radius = 1.
sphere1 = Sphere(origin, radius)
sphere1.set_color(edge_color = (255, 255, 255), in_color = (128, 255, 0))

# sphere with blue edge and yellow inside
origin = Vector3(1, -1, 1)
radius = 1.
sphere2 = Sphere(origin, radius)
sphere2.set_color(edge_color = (0, 128, 255), in_color = (204, 204, 0))

def sample1():
    '''
    parallel, 2 spheres
    '''
    # build camera
    e = Vector3(0, 0, 2) # e is the view point of camera, i.e. "origin"
    w = Vector3(-1, 0, 0) # w is the opposite of viewing direction
    up = Vector3(0, 1, 0) # "up" vector
    camera = ParallelCamera(e, w, up)
    camera.set_size(l = -1.5, r = 1.5, b = -1.5, t = 1.5) # left, right, bottom, top spans w.r.t to e

    # setup tracer
    tracer = Tracer(camera, [sphere1, sphere2])
    tracer.render('sample1.png', (512, 512)) # 2nd argument is the pixel size of the output graph

if __name__ == '__main__':
    sample1()
