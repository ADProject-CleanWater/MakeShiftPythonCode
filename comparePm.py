
class ComparePm():
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def ComparePM(self):
        if self.key == "pm10":
            if self.data < 30 : return "좋음"
            elif self.data < 80 : return "보통"
            elif self.data < 150 : return "나쁨"
            else : return "매우 나쁨"
        elif self.key == "pm25":
            if self.data < 15 : return "좋음"
            elif self.data < 35 : return "보통"
            elif self.data < 75 : return "나쁨"
            else : return "메우 나쁨"
