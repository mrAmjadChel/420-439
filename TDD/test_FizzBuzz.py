from unittest import result
from FizzBuss import FizzBuzz

import unittest
class FizzbuzzTest(unittest.TestCase):
    def test_give_3_(self):
        num = 5
        result = FizzBuzz(num)
        self.assertEqual(result,"Buzz")