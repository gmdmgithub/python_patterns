# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug - unit test assert functions

# name convention of files is important

# python -m unittest #in the directory - but after adding '__main__' - it works like ordinary 

import unittest
import simple

class TestSimple(unittest.TestCase):
    def test_add(self): #name convetion is important
        result = simple.add(7,5)
        self.assertEqual(result,12)

    def test_subtract(self):
        self.assertEqual(simple.subtract(12,14),-2)
        self.assertEqual(simple.subtract(-1, 1), -2)
        self.assertEqual(simple.subtract(-1, -1), 0)
    def test_multiply(self):
        self.assertEqual(simple.multiply(7, 5), 35)
        self.assertEqual(simple.multiply(-1, 1), -1)
        self.assertEqual(simple.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(simple.divide(10, 5), 2)
        self.assertEqual(simple.divide(-1, 1), -1)
        self.assertEqual(simple.divide(-1, -1), 1)
        self.assertEqual(simple.divide(10, 4), 2.5)

        with self.assertRaises(ValueError):
            simple.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
