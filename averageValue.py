# 데이터베이스와 키값을 받고 value의 평균을 구하는 class

class AverageValue():
    def __init__(self, listDB, key):
        self.listDB = listDB
        self.key = key
        self.sortList = []

        self.DataInList()

    def DataInList(self):
        for i in range(len(self.listDB)):
            self.sortList.append(int(self.listDB[i][self.key]))

    def AverValue(self):
        num = sum(self.sortList)
        return round(num / len(self.sortList), 4)

    def lastValue(self):
        return self.sortList[len(self.sortList)-1]



