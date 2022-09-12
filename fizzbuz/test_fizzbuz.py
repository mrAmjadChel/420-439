from fizzbuz.fizzbuz import fizzbuzz

import unittest

class FizzbuzzTest(unittest.TestCase):
    def test_3_is_Fizz(self):    
        number = 3
        result = fizzbuzz(number)
        self.assertNotEqual(result ,"FizzBuzz!")

    
    