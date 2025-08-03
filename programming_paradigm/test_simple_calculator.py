import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(-5,-3),-8)
        self.assertEqual(self.calc.add(0,0),0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(3,5),-2)
        self.assertEqual(self.calc.subtract(-5,-3),-2)
        self.assertEqual(self.calc.subtract(0,0),0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,3),12)
        self.assertEqual(self.calc.multiply(-2,3),-6)
        self.assertEqual(self.calc.multiply(0,10),0)
        self.assertEqual(self.calc.multiply(-2,-3),6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(-10,2),-5)
        self.assertEqual(self.calc.divide(-9,-3),3)
        self.assertEqual(self.calc.divide(0,3),0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10,0))
        self.assertIsNone(self.calc.divide(0,0))

if __name__ == '__main__':
    unittest.main()
