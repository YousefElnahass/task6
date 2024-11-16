import unittest
from calc import add
#mohamed yehia 221001815             youssef nasr            221000911
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 1), 4)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -2), -7)
        self.assertEqual(add(4, -2), 2)
        

if __name__ == '__main__':
    unittest.main()
