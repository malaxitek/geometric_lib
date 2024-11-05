import unittest

def area(a):
    return a * a


def perimeter(a):
    return 4 * a


class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10)
       self.assertEqual(res, 100)

   def test_negative_mul(self):
        res = area(-10)
        self.assertEqual(res, 0)
    
   def test_zero_per(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
   def test_square_per(self):
       res = perimeter(10)
       self.assertEqual(res, 40)

   def test_negative_per(self):
        res = perimeter(-10)
        self.assertEqual(res, 0)
