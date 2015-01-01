A plain ray tracing program using pixel drawing only, i.e. no graphics APIs like openGL involved.

No shading is implemented as of now.

Customizable colors (both edge and within) for objects.

###Supporting features(crossed are completed): 
* ~~parallel~~ & perpective projection
* ~~orthographic~~ & oblique
* shapes: ~~sphere~~, ~~triangle~~, polygon

###User input: (see `main.py`)
* shapes with specifications
* image plane: v & up vector, width and height span
* output file and pixel size
* parallel or perspective camera
* projection direction (orthogonal in default)

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
