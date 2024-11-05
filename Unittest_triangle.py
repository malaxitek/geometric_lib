import unittest

def area(a, h):
    return a * h / 2 

def perimeter(a, b, c):
    return a + b + c

class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0, 5)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 5)
       self.assertEqual(res, 25)

   def test_negative_mul(self):
        res = area(-10, 5)
        self.assertEqual(res, 0)
    
   def test_zero_per(self):
       res = perimeter(20, 4, 5)
       self.assertEqual(res, 0)
       
   def test_square_per(self):
       res = perimeter(10, 6, 6)
       self.assertEqual(res, 22)

   def test_negative_per(self):
        res = perimeter(-10, 4, 12)
        self.assertEqual(res, 0)
