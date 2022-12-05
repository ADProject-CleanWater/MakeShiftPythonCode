import unittest

from comparePm import ComparePm

class TestCompare(unittest.TestCase):
    def setUp(self):
        self.g1 = ComparePm(29, "pm10")
        self.g2 = ComparePm(79, "pm10")
        self.g3 = ComparePm(149, "pm10")
        self.g4 = ComparePm(151, "pm10")
        self.g5 = ComparePm(14, "pm25")
        self.g6 = ComparePm(34, "pm25")
        self.g7 = ComparePm(74, "pm25")
        self.g8 = ComparePm(76, "pm25")

    def tearDown(self):
        print("This is tear down")
        
    def testComparePM(self):
        self.assertEqual(self.g1.ComparePM(), "좋음")
        self.assertEqual(self.g2.ComparePM(), "보통")
        self.assertEqual(self.g3.ComparePM(), "나쁨")
        self.assertEqual(self.g4.ComparePM(), "매우 나쁨")
        self.assertEqual(self.g5.ComparePM(), "좋음")
        self.assertEqual(self.g6.ComparePM(), "보통")
        self.assertEqual(self.g7.ComparePM(), "나쁨")
        self.assertEqual(self.g8.ComparePM(), "매우 나쁨")



if __name__ == "__main__":
    unittest.main()