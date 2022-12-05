import unittest

from showDB import ShowDB

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

class TestShowDB(unittest.TestCase):
    def setUp(self):
        self.g1 = ShowDB(TestList1, "Test1")
        self.g2 = ShowDB(TestList1, "Test2")

    def tearDown(self):
        print("This is tear down")

    def testGetSortList(self):
        self.g1.InputSortList()
        self.assertEqual(self.g1.getSortList(),
                         ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29']
                         )
        self.g2.InputSortList()
        self.assertEqual(self.g2.getSortList(),
                         ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30']
                         )

if __name__ == "__main__":
    unittest.main()