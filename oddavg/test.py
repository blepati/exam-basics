import unittest
from odd_avg import odd_average

class AverageMethod(unittest.TestCase):

    def test_average(self):
        list_of_nums = [9, 9, 10, 9, 3]
        self.assertEqual(odd_average(list_of_nums), 9)

    def test_odds(self):
        list_of_nums = [4, 6, 8]
        self.assertEqual(odd_average(list_of_nums), 0)

    def test_empty_list(self):
        list_of_nums = [ ]
        self.assertEqual(odd_average(list_of_nums), None)

if __name__ == '__main__':
    unittest.main()
