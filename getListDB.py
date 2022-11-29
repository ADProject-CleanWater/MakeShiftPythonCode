from showDB import ShowDB

class GetListDB():
    def __init__(self, list):
        self.listDB = list

    def sortedListDB_X(self, key):
        self.getList_X = []
        showDB = ShowDB(self.listDB, key)
        showDB.InputSortList()
        d = showDB.getSortList()
        for i in range(len(d)):
            self.getList_X.append(float(i+1))

        return self.getList_X

    def sortedListDB_Y(self, key):
        self.getList_Y = []
        showDB = ShowDB(self.listDB, key)
        showDB.InputSortList()
        d = showDB.getSortList()
        for i in range(len(d)):
            self.getList_Y.append(float(d[i]))

        return self.getList_Y