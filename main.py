#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shape import *

def main():
    circle1 = Circle()
    circle1.radius = 5.
    circle1.center = Point(2., 3.)

    print "Circle1 :"
    circle1.show()

    circle2 = Circle()
    circle2.radius = 3.
    circle2.center = Point(1., 1.)

    print "Circle2 :"
    circle2.show()

    composition1 = Composition()
    composition1.addShape(circle1)
    composition1.addShape(circle2)

    print "Composition1 :"
    composition1.show()

    rectangle1 = Rectangle()
    rectangle1.frame = Rect(Point(2., 2.), Size(5., 18.))

    rectangle2 = Rectangle()
    rectangle2.frame = Rect(Point(6., 12.), Size(4., 4.))

    square1 = Square()
    square1.origin = Point(4., 4.)
    square1.size = 85.

    composition2 = Composition()
    composition2.addShape(rectangle2)
    composition2.addShape(square1)

    print "Composition2 :"
    composition2.show()

    composition1.addShape(rectangle1)
    composition1.addShape(composition2)

    print "Composition1 with Composizton 2 inside: "
    composition1.show()

if __name__ == '__main__':
    main()
