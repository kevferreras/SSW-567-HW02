# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right: 3,4,5 is a Right Triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(4,3,5),'Right: 4,3,5 is a Right Triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral: 1,1,1 is an Equilateral Triangle')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(7,7,4), 'Isosceles: 7,7,4 is an Isosceles Triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(6,5,7), 'Scalene: 6,5,7 is a Scalene Triangle')

    def testInputsGreaterThan200(self):
        self.assertEqual(classifyTriangle(300,40,50), 'Invalid Input')
        self.assertEqual(classifyTriangle(70,700,40), 'Invalid Input')
        self.assertEqual(classifyTriangle(50,30,400), 'Invalid Input')
        self.assertEqual(classifyTriangle(600,600,600), 'Invalid Input')
        self.assertEqual(classifyTriangle(201,40,40), 'Invalid Input')
        self.assertEqual(classifyTriangle(50,201,40), 'Invalid Input')
        self.assertEqual(classifyTriangle(20,40,201), 'Invalid Input')

    def testNegativeInputs(self):
        self.assertEqual(classifyTriangle(-3,4,5), 'Invalid Input')
        self.assertEqual(classifyTriangle(7,-7,4), 'Invalid Input')
        self.assertEqual(classifyTriangle(5,3,-4), 'Invalid Input')
        self.assertEqual(classifyTriangle(-1,-1,-1), 'Invalid Input')

    def testDecimalInputs(self):
        self.assertEqual(classifyTriangle(3.2,4,5), 'Invalid Input')
        self.assertEqual(classifyTriangle(7,7.1,4), 'Invalid Input')
        self.assertEqual(classifyTriangle(5,3,4.0), 'Invalid Input')
        self.assertEqual(classifyTriangle(1.5,1.5,1.5), 'Invalid Input')

    def testSumOfTwoSides(self):
        self.assertEqual(classifyTriangle(3,4,9), 'Not A Triangle')
        self.assertEqual(classifyTriangle(2,4,7), 'Not A Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

