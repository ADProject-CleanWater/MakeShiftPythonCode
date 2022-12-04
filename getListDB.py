from showDB import ShowDB

class GetListDB():
    def __init__(self, list):
        self.listDB = list
        self.value = -1

    def getValue(self, value):
        self.value = value

    def sortedListDB_X(self, key):
        if key == '개월':
            self.getList_X = []
            showDB = ShowDB(self.listDB, key)
            showDB.InputSortList()
            d = showDB.getSortList()
            for i in range((self.value - 2007) * 12):
                if len(d) > i :
                    self.getList_X.append(float(i+1))
        else :
            self.getList_X = []
            showDB = ShowDB(self.listDB, key)
            showDB.InputSortList()
            d = showDB.getSortList()
            for i in range(len(d)):
                self.getList_X.append(float(i+1))

        return self.getList_X

    def sortedListDB_Y(self, key):
        if key == 'temp 평균' or key == 'humi 평균':
            self.getList_Y = []
            showDB = ShowDB(self.listDB, key)
            showDB.InputSortList()
            d = showDB.getSortList()
            for i in range((self.value - 2007) * 12):
                if len(d) > i:
                    self.getList_Y.append(float(d[i]))
        else :
            self.getList_Y = []
            showDB = ShowDB(self.listDB, key)
            showDB.InputSortList()
            d = showDB.getSortList()
            for i in range(len(d)):
                self.getList_Y.append(float(d[i]))

        return self.getList_Y