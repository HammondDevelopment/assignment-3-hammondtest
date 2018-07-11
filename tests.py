import unittest
from assignment3 import addOne, addTwo, divide

class Assignment3Tests(unittest.TestCase):
  def testOne(self):
    self.assertEqual(addOne(1), 2)
  
  def testTwo(self):
    self.assertEqual(addTwo(1), 3)

  def testDivide(self):
    self.assertEqual(divide(4, 2), 2)
    with self.assertRaises(ZeroDivisionError):
      x = divide(2, 0)

if __name__ == '__main__':
  unittest.main()