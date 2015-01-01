'''
main tracer class
'''
from PIL import Image
from colors import BLACK

import pdb

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
                # check intersection and take closest hit
                hit_point = float('inf')
                pixel = BLACK
                for shape in self.shapes:
                    hit, t = shape.intersect(ray)
                    if hit == 1 and t < hit_point: #inner
                        hit_point = t
                        pixel = shape.in_color
                    elif hit == 0 and t < hit_point: #edge
                        hit_point = t
                        pixel = shape.edge_color
                
                pixels.append(pixel)
        
        image.putdata(pixels)
        image.save(outputname)
