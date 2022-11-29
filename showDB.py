#리스트 내 딕셔너리의 키 값을 입력하면 벨류를 출력


class ShowDB():
    def __init__(self, listDB, key):
        self.key = key
        self.listDB = listDB
        self.sortList = []

    def InputSortList(self):
        for i in range(len(self.listDB)):
            self.sortList.append(self.listDB[i][self.key])

    def getSortList(self):
        return self.sortList


