import unittest
from utils import fact

class FactTest(unittest.TestCase):

    def test_simple_value(self):
        self.assertEquals(fact(0), 1)

    def test_some_number(self):
        self.assertEquals(fact(4), 24)

    def test_value_error(self):
        self.assertRaises(ValueError, fact, -10)

if __name__ == "__main__":
    unittest.main()