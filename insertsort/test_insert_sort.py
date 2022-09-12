import random
from insert_sort import insertion_sort
data = [-999, 16, 2, 8, 50, 35]
data = insertion_sort(data)
for i in data:
    print(i)

import unittest

class test_insertionsort(unittest.TestCase):
    def test_insertionsort(self):
        "Test insertion_sort()"
        data = [random.randrange(-1000, 1000) for _ in range(1000)]
        self.assertEqual(insertion_sort(data), sorted(data))

