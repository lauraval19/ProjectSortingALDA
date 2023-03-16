import unittest

from sortalgorithms.algorithms import *

arrays = [
    [1, 9, 8, 2, 3, 4, 5, 7, 6],
    [1],
    [2],
    [-11, 10, 25, 100, -500, 300, -250, 1000],
    [10, 8],
]
expected = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1],
    [2],
    [-500, -250, -11, 10, 25, 100, 300, 1000],
    [8, 10],
]


class AlgorithmsTest(unittest.TestCase):
    def test_selection_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = selection_sort(array)
            self.assertTrue(result, expected[i])

    def test_merge_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = merge_sort(array)
            self.assertTrue(result, expected[i])

    def test_insertion_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = insertion_sort(array)
            self.assertTrue(result, expected[i])


if __name__ == "__main__":
    unittest.main()
