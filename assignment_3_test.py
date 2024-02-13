import unittest
from assignment_3 import *

class MyTestCase(unittest.TestCase):
    def test_sort_number(self):
        arr = [3, 2, 5, 1, 8, 9, 6]
        expectedRes = [8,6,2,9,5,3,1]
        arr = sort_number(arr)
        self.assertEqual(arr, expectedRes)


if __name__ == '__main__':
    unittest.main()
