A plain ray tracing program using pixel drawing only, i.e. no graphics APIs like openGL involved.

No shading is implemented as of now.

###How to use

* run tests: `python test.py`
* refer to `main.py` to see how to config camera, create scenes, and render the scene (`python main.py`).  

###Supporting features(crossed are completed): 
* ~~parallel~~ & perpective projection
* ~~orthographic~~ & oblique
* shapes: ~~sphere~~, ~~triangle~~, polygon

###Config camera and setup scene: (see `main.py`)
* shapes in scene: origin, size, color -- both edge and inner color)
* camera: v & up vector, width and height span; parallel or perspective; projection direction (orthogonal in default)
* output file: path and pixel size

###Requirements:
* pillow: `pip install pillow`

###Todo:
* edge detection on triangles & polygons
* ~~bug with triangle projection T.T~~

###References & credits: 
* Fundamentals of Computer Graphics, Chapter 4
* [PIL Image class](https://pillow.readthedocs.org/reference/Image.html)
* [How to draw pixels in PIL](http://stackoverflow.com/questions/434583/what-is-the-fastest-way-to-draw-an-image-from-discrete-pixel-values-in-python)
* [Nice color picker](http://www.rapidtables.com/web/color/RGB_Color.htm)

###Examples

* simple parallel & orthogonal projection on two overlapping spheres (see `sample1()` in `main.py`)

![normal](sample1.png?raw=true)

* parallel & orthogonal projection on overlapping sphere and triangle (see `sample2()` in `main.py`)

![normal](sample2.png?raw=true)
