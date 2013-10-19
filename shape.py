# -*- coding: utf-8 -*-

import zope.interface


class Point(object):
    def __init__(self, x = 0., y = 0.):
        super(Point, self).__init__()
        self.x = x
        self.y = y;


class Size(object):
    def __init__(self, width = 0., height = 0.):
        super(Size, self).__init__()
        self.width = width
        self.height = height


class Rect(object):
    def __init__(self, origin = None, size = None):
        super(Rect, self).__init__()
        self.origin = origin
        self.size = size


class IShape(zope.interface.Interface):
    """This is interface class of shapes"""

    def show(self):
        pass

    def move(self, point):
        pass


class Circle(object):
    zope.interface.implements(IShape)

    center = Point()
    radius = 0.

    def show(self):
        print "Circle. Center: %f, %f; Radius: %f" % (self.center.x, self.center.y, self.radius)

    def move(self, point):
        self.center.x += point.x;
        self.center.y += point.y;


class Rectangle(object):
    zope.interface.implements(IShape)

    frame = Rect(Point(0., 0.), Size(0., 0.))

    def show(self):
        print "Rectangle. Frame (%f, %f, %f, %f)" % (self.frame.origin.x, self.frame.origin.y, self.frame.size.width, self.frame.size.height)

    def move(self, point):
        self.frame.origin.x += point.x;
        self.frame.origin.y += point.y;


class Square(Rectangle):

    origin = Point(0., 0.)
    size = 0.

    def show(self):
        print "Square. Orifin: %f, %f; Size: %f" % (self.origin.x, self.origin.y, self.size)

    def move(self, point):
        pass


class Composition(object):
    zope.interface.implements(IShape)

    shapes = []

    def __init__(self):
        super(Composition, self).__init__()
        self.shapes = []

    def show(self):
        print "Begin composition"
        for shape in self.shapes:
            shape.show()
        print "End composition"

    def move(self, point):
        for shape in self.shapes:
            shape.move(point)


    def addShape(self, shape):
        self.shapes.append(shape)

    def removeShapeAtIndex(self, index):
        del self.shapes[index]


assert IShape.implementedBy(Circle)
assert IShape.implementedBy(Rectangle)
assert IShape.implementedBy(Composition)
