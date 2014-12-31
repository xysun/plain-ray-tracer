'''
main tracer class
'''
from PIL import Image

import pdb

BLACK = (0,0,0)

class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

class Tracer(object):
    def __init__(self, camera, shapes):
        '''
        shapes: [shape]
        '''
        self.camera = camera
        self.shapes = shapes
        pass
    
    def render(self, outputname, size):
        '''
        outputname: name of output image
        size: (w,h), size of output image in pixels
        '''
        image = Image.new('RGB', size)

        pixels = []
        nx = size[0]
        ny = size[1]
        for j in range(0, ny):
            for i in range(0, nx):
                # compute ray
                ray = self.camera.compute_ray(i, j, nx, ny)
                # check intersection
                # TODO: take closest hit
                for shape in self.shapes:
                    hit = shape.intersect(ray)
                    if hit > 0: # inner
                        pixels.append(shape.in_color)
                    elif hit == 0: # edge
                        # print "edge!"
                        pixels.append(shape.edge_color)
                    else: # black
                        pixels.append(BLACK)
        
        image.putdata(pixels)
        image.save(outputname)
