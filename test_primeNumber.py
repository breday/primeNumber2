import unittest
from primeNumber import primeNum


class primeTestCase(unittest.TestCase):
    """Testing orimeNumber.py`."""

    def test_primeNum_odd_prime(self):
        """test if 7 is a prime number"""
        self.assertTrue(primeNum(7))

    def test_primeNum_even_on_prime(self):
        """test if 28 is not a prime number"""
        self.assertFalse(primeNum(28), msg='28 is not prime!')

    def test_primeNum_eight_non_prime(self):
        """test if 8 is not a prime number"""
        self.assertFalse(primeNum(8), msg='Eight is not prime!')

    def test_primeNum_zero_non_prime(self):
        """test if zero is not a prime number"""
        self.assertFalse(primeNum(0), msg='zero is not prime!')

    def test_negative_number(self):
        """test if negative numbers are not  prime"""
        for index in range(-1, -10, -1):
            self.assertFalse(primeNum(index))

if __name__ == '__main__':
unittest.main()