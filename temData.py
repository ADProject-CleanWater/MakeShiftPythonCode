from show import PMS, BMS
from showDB import ShowDB
from averageValue import AverageValue
from comparePm import ComparePm

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.sc = MplCanvas()
        self.draw_graph_pm10()
        toolbar = NavigationToolbar(self.sc, self)

        self.tempText = QLineEdit()
        self.tempText.setReadOnly(True)
        self.tempText.setAlignment(Qt.AlignLeft)
        font = self.tempText.font()
        font.setFamily('Courier New')
        self.tempText.setFont(font)
        self.tempText.setStyleSheet('color:black;font-size:18px;')
        self.tempText.setFixedSize(200, 100)
        self.tempAver = AverageValue(BMS, "temp")
        self.tempText.setText("온도 : " + str(self.tempAver.AverValue()))

        self.humiText = QLineEdit()
        self.humiText.setReadOnly(True)
        self.humiText.setAlignment(Qt.AlignLeft)
        font = self.humiText.font()
        font.setFamily('Courier New')
        self.humiText.setFont(font)
        self.humiText.setStyleSheet('color:black;font-size:18px;')
        self.humiText.setFixedSize(200, 100)
        self.humiAver = AverageValue(BMS, "humi")
        self.humiText.setText("습도 : " + str(self.humiAver.AverValue()))

        self.nowPmText = QTextEdit()
        self.nowPmText.setReadOnly(True)
        self.nowPmText.setAlignment(Qt.AlignLeft)
        font = self.nowPmText.font()
        font.setFamily('Courier New')
        self.nowPmText.setFont(font)
        self.nowPmText.setStyleSheet('color:black;font-size:18px;')
        self.nowPmText.setFixedSize(200, 100)
        self.pmAver = AverageValue(PMS, "pm10")
        self.comPM = ComparePm(self.pmAver.lastValue(), "pm10")
        self.nowPmText.setText("현재 미세먼지 농도는 \n" + self.comPM.ComparePM() + "(" +str(self.pmAver.lastValue()) + ") 입니다.")

        self.pmText = QTextEdit()
        self.pmText.setReadOnly(True)
        self.pmText.setAlignment(Qt.AlignRight)
        font = self.pmText.font()
        font.setFamily('Courier New')
        self.pmText.setFont(font)
        self.pmText.setStyleSheet('color:black;font-size:18px;')
        self.pmText.setFixedSize(200, 200)
        self.pmText.setText("<PM10>\n좋음 : 0 ~ 30 \n보톰 : 31 ~ 80\n나쁨 : 81 ~ 150\n매우 나쁨 : 151이상")

        pm10Button = QPushButton('PM10')
        pm10Button.clicked.connect(self.draw_graph_pm10)
        pm10Button.clicked.connect(self.text_pm10)
        pm25Button = QPushButton('PM25')
        pm25Button.clicked.connect(self.draw_graph_pm25)
        pm25Button.clicked.connect(self.text_pm25)

        hBoxButton = QHBoxLayout()
        hBoxButton.addStretch(2)
        hBoxButton.addWidget(pm10Button)
        hBoxButton.addWidget(pm25Button)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(toolbar)
        leftLayout.addWidget(self.sc)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.tempText)
        rightLayout.addStretch(1)
        rightLayout.addWidget(self.humiText)
        rightLayout.addStretch(1)
        rightLayout.addWidget(self.nowPmText)
        rightLayout.addStretch(1)
        rightLayout.addWidget(self.pmText)
        rightLayout.addLayout(hBoxButton)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)


        self.setLayout(mainLayout)
        self.show()

    def draw_graph_pm10(self):
        getListDB = GetListDB()
        key = 'pm10'
        self.sc.axes.cla()
        self.sc.axes.plot(getListDB.sortedListDB_X(key), getListDB.sortedListDB_Y(key))
        self.sc.axes.set_xlabel("ID")
        self.sc.axes.set_ylabel(key)
        self.sc.axes.grid()
        self.sc.draw()

    def draw_graph_pm25(self):
        getListDB = GetListDB()
        key = 'pm25'
        self.sc.axes.cla()
        self.sc.axes.plot(getListDB.sortedListDB_X(key), getListDB.sortedListDB_Y(key))
        self.sc.axes.set_xlabel("ID")
        self.sc.axes.set_ylabel(key)
        self.sc.axes.grid()
        self.sc.draw()

    def text_pm10(self):
        key = "pm10"
        self.pmAver = AverageValue(PMS, key)
        self.comPM = ComparePm(self.pmAver.lastValue(), key)
        self.nowPmText.setText("현재 미세먼지 농도는 \n" + self.comPM.ComparePM() + "(" + str(self.pmAver.lastValue()) + ") 입니다.")
        self.pmText.setText("<PM10>\n좋음 : 0 ~ 30 \n보톰 : 31 ~ 80\n나쁨 : 81 ~ 150\n매우 나쁨 : 151이상")

    def text_pm25(self):
        key = "pm25"
        self.pmAver = AverageValue(PMS, key)
        self.comPM = ComparePm(self.pmAver.lastValue(), key)
        self.nowPmText.setText("현재 미세먼지 농도는 \n" + self.comPM.ComparePM() + "(" + str(self.pmAver.lastValue()) + ") 입니다.")
        self.pmText.setText("<PM2.5>\n좋음 : 0 ~ 15 \n보톰 : 15 ~ 35\n나쁨 : 36 ~ 75\n매우 나쁨 : 76이상")

class GetListDB():
    def __init__(self):
        self.listDB = PMS

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


if __name__=="__main__" :
   app = QApplication(sys.argv)
   main = Main()
   sys.exit(app.exec_())