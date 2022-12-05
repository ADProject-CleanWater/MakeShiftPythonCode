import unittest

from averageValue import AverageValue

TestList1 = [
    {"Test1": "1", "Test2": "2"},
    {"Test1": "3", "Test2": "4"},
    {"Test1": "5", "Test2": "6"},
    {"Test1": "7", "Test2": "8"},
    {"Test1": "9", "Test2": "10"},
    {"Test1": "11", "Test2": "12"},
    {"Test1": "13", "Test2": "14"},
    {"Test1": "15", "Test2": "16"},
    {"Test1": "17", "Test2": "18"},
    {"Test1": "19", "Test2": "20"},
    {"Test1": "21", "Test2": "22"},
    {"Test1": "23", "Test2": "24"},
    {"Test1": "25", "Test2": "26"},
    {"Test1": "27", "Test2": "28"},
    {"Test1": "29", "Test2": "30"}
]

class TestAverageValue(unittest.TestCase):
    def setUp(self):
        self.g1 = AverageValue(TestList1, "Test1")
        self.g2 = AverageValue(TestList1, "Test2")

    def tearDown(self):
        print("This is tear down")

    def testAverValue(self):
        self.assertEqual(self.g1.AverValue(), 15.0)
        self.assertEqual(self.g2.AverValue(), 16.0)

    def testLastValue(self):
        self.assertEqual(self.g1.lastValue(), 29.0)
        self.assertEqual(self.g2.lastValue(), 30.0)

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
