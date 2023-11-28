import unittest

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n-1)

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
