import unittest
from main import add
from main import subtract
from main import multiply
from main import divide

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(1, 1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(-1, -1), 1.0)
        

if __name__ == '__main__':
    unittest.main()