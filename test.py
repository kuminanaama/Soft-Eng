import unittest
from example import find_fixed_point

class TestfindFixedPoint(unittest.TestCase):

    def test_numbers(self):
        A = [-10, -5, 0, 3, 7]
        result = find_fixed_point(A)
        self.assertEqual(result,3)



    def test_no_fixed_point(self):
        A = [1, 2, 3, 4, 5]
        result = find_fixed_point(A)
        self.assertEqual(result, -1)  

if __name__ == '__main__':
    unittest.main()