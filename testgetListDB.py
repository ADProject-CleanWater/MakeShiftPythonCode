import unittest

from getListDB import GetListDB

TestList1 = [
    {"Test1": "1", "Test2": "2", "개월": "1", 'temp 평균': '1'},
    {"Test1": "3", "Test2": "4", "개월": "2", 'temp 평균': '2'},
    {"Test1": "5", "Test2": "6", "개월": "3", 'temp 평균': '3'},
    {"Test1": "7", "Test2": "8", "개월": "4", 'temp 평균': '4'},
    {"Test1": "9", "Test2": "10", "개월": "5", 'temp 평균': '5'},
    {"Test1": "11", "Test2": "12", "개월": "6", 'temp 평균': '6'},
    {"Test1": "13", "Test2": "14", "개월": "7", 'temp 평균': '7'},
    {"Test1": "15", "Test2": "16", "개월": "8", 'temp 평균': '8'},
    {"Test1": "17", "Test2": "18", "개월": "9", 'temp 평균': '9'},
    {"Test1": "19", "Test2": "20", "개월": "10", 'temp 평균': '10'},
    {"Test1": "21", "Test2": "22", "개월": "11", 'temp 평균': '11'},
    {"Test1": "23", "Test2": "24", "개월": "12", 'temp 평균': '12'},
    {"Test1": "25", "Test2": "26", "개월": "13", 'temp 평균': '13'},
    {"Test1": "27", "Test2": "28", "개월": "14", 'temp 평균': '14'},
    {"Test1": "29", "Test2": "30", "개월": "15", 'temp 평균': '15'}
]

class TestGetListDB(unittest.TestCase):
    def setUp(self):
        self.g1 = GetListDB(TestList1)

    def tearDown(self):
        print("This is tear down")
        pass

    def testGetValue(self):
        self.assertEqual(self.g1.getValue("Test"), "Test")

    def testSortedListDB_X(self):
        self.assertEqual(self.g1.sortedListDB_X("Test1"),
                         [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
                         )
        self.assertEqual(self.g1.sortedListDB_X("Test2"),
                         [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
                         )
        self.g1.getValue(2008)
        self.assertEqual(self.g1.sortedListDB_X("개월"),
                         [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
                         )
        self.g1.getValue(2009)
        self.assertEqual(self.g1.sortedListDB_X("개월"),
                         [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
                         )

    def testSortedListDB_Y(self):
        self.assertEqual(self.g1.sortedListDB_Y("Test1"),
                         [1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0]
                         )
        self.assertEqual(self.g1.sortedListDB_Y("Test2"),
                         [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0]
                         )
        self.g1.getValue(2008)
        self.assertEqual(self.g1.sortedListDB_Y("temp 평균"),
                         [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
                         )
        self.g1.getValue(2009)
        self.assertEqual(self.g1.sortedListDB_Y("temp 평균"),
                         [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
                         )

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
