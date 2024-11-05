import unittest

def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_negative_mul(self):
        res = area(-10, 10)
        self.assertEqual(res, 0)
    
   def test_zero_per(self):
       res = perimeter(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_per(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)

   def test_negative_per(self):
        res = perimeter(-10, 10)
        self.assertEqual(res, 0)
