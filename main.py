'''
samples of how to piece everything together
'''
from camera import ParallelCamera
from shapes import Sphere, Triangle
from tracer import Tracer
from vector import Vector3

from colors import *

# factories of shapes

# sphere with white edge and green inside
origin = Vector3(2, 0, 2)
radius = 1.
sphere1 = Sphere(origin, radius)
sphere1.set_color(edge_color = WHITE, in_color = GREEN)

# sphere with blue edge and yellow inside
origin = Vector3(1, -1, 1)
radius = 1.
sphere2 = Sphere(origin, radius)
sphere2.set_color(edge_color = BLUE, in_color = YELLOW)

# a right triangle
triangle1 = Triangle(Vector3(4, 0, 0), Vector3(4, 2, 2), Vector3(4, 0, 2))
triangle1.set_color(edge_color = BLUE, in_color = YELLOW)

# a distorted triangle
triangle2 = Triangle(Vector3(2, 0, 0), Vector3(2, 2, 2), Vector3(4, 0, 2))
triangle2.set_color(edge_color = BLUE, in_color = YELLOW)

# camera1, parallel
e = Vector3(0, 0, 2) # e is the view point of camera, i.e. "origin"
w = Vector3(-1, 0, 0) # w is the opposite of viewing direction
up = Vector3(0, 1, 0) # "up" vector
camera1 = ParallelCamera(e, w, up)

# camera2
e = Vector3(0, 0, 2) 
w = Vector3(-1, 0, 0) 
up = Vector3(0, 1, 0) 
camera2 = ParallelCamera(e, w, up)


def sample1():
    '''
    parallel, 2 spheres
    '''
    camera = camera1
    camera.set_size(l = -1.5, r = 1.5, b = -1.5, t = 1.5) # left, right, bottom, top spans w.r.t to e

    # setup tracer
    tracer = Tracer(camera, [sphere1, sphere2])
    tracer.render('sample1.png', (512, 512)) # 2nd argument is the pixel size of the output graph

def sample2():
    '''
    parallel, triangle + sphere
    '''
    camera = camera1
    camera.set_size(l = -1.5, r = 1.5, b = -1.5, t = 1.5)

    tracer = Tracer(camera, [sphere1, triangle2])
    tracer.render('sample2.png', (512, 512))

def test():
    camera = camera2
    camera.set_size(l = -1.5, r = 1.5, b = -1.5, t = 1.5)

    tracer = Tracer(camera, [sphere1, triangle2])
    tracer.render('testsample.png', (512, 512))


if __name__ == '__main__':
    #sample1()
    sample2()
    #test()
