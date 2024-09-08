import unittest

# This is the class where you'll write your test cases.
class TestMyFunction(unittest.TestCase):
    
    # This is a test case method.
    def test_addition(self):
        result = 1 + 1
        self.assertEqual(result, 2)  # This asserts that the result should be 2

    def test_subtraction(self):
        result = 2 - 1
        self.assertEqual(result, 1)  # This asserts that the result should be 1

if __name__ == '__main__':
    unittest.main()
