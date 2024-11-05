import math
import unittest

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(3)
       self.assertEqual(res, 28,274333882308137)

   def test_negative_mul(self):
        res = area(-10)
        self.assertEqual(res, 0)
    
   def test_zero_per(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
   def test_square_per(self):
       res = perimeter(3)
       self.assertEqual(res, 18,849555921538758)

   def test_negative_per(self):
        res = perimeter(-10)
        self.assertEqual(res, 0)
