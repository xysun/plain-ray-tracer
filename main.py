'''
samples of how to piece everything together
'''
from camera import ParallelCamera
from shapes import Sphere
from tracer import Tracer
from vector import Vector3

def sample1():
    '''
    parallel, sphere
    '''
    # build sphere with white edge and green inside
    origin = Vector3(2, 0, 2)
    radius = 1.
    sphere = Sphere(origin, radius)
    sphere.set_color(edge_color = (255, 255, 255), in_color = (128, 255, 0))

    # build camera
    e = Vector3(0, 0, 2)
    w = Vector3(-1, 0, 0)
    up = Vector3(0, 1, 0)
    camera = ParallelCamera(e, w, up)
    camera.set_size(l = -1.5, r = 1.5, b = -1.5, t = 1.5)

    # setup tracer
    tracer = Tracer(camera, [sphere])
    tracer.render('sample1.png', (512, 512))

if __name__ == '__main__':
    sample1()
