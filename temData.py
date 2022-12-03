import show
from averageValue import AverageValue
from comparePm import ComparePm
from getListDB import GetListDB

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import importlib

#데이터를 실시간으로 적용
#년별 매월 그래프 구현 2008~2021 온도 비교

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.key = "pm10"
        self.check = True

        self.init_ui()

    def init_ui(self):
        self.sc = MplCanvas()
        self.draw_graph()
        toolbar = NavigationToolbar(self.sc, self)

        self.tempText = QLineEdit()
        self.tempText.setReadOnly(True)
        self.tempText.setAlignment(Qt.AlignLeft)
        font = self.tempText.font()
        font.setFamily('Courier New')
        self.tempText.setFont(font)
        self.tempText.setStyleSheet('color:black;font-size:28px;')
        self.tempText.setFixedSize(300, 100)

        self.humiText = QLineEdit()
        self.humiText.setReadOnly(True)
        self.humiText.setAlignment(Qt.AlignLeft)
        font = self.humiText.font()
        font.setFamily('Courier New')
        self.humiText.setFont(font)
        self.humiText.setStyleSheet('color:black;font-size:28px;')
        self.humiText.setFixedSize(300, 100)

        self.nowPmText = QTextEdit()
        self.nowPmText.setReadOnly(True)
        self.nowPmText.setAlignment(Qt.AlignLeft)
        font = self.nowPmText.font()
        font.setFamily('Courier New')
        self.nowPmText.setFont(font)
        self.nowPmText.setStyleSheet('color:black;font-size:20px;')
        self.nowPmText.setFixedSize(300, 100)

        self.pmText = QTextEdit()
        self.pmText.setReadOnly(True)
        self.pmText.setAlignment(Qt.AlignRight)
        font = self.pmText.font()
        font.setFamily('Courier New')
        self.pmText.setFont(font)
        self.pmText.setStyleSheet('color:black;font-size:20px;')
        self.pmText.setFixedSize(300, 200)

        self.textPM()

        pm10Button = QPushButton('PM10')
        pm10Button.clicked.connect(self.push_button_pm10)
        pm25Button = QPushButton('PM25')
        pm25Button.clicked.connect(self.push_button_pm25)
        comTempButton = QPushButton('Temp')
        comTempButton.clicked.connect(self.push_button_compareTemp)
        self.comboBoxYear()

        hBoxButton = QHBoxLayout()
        hBoxButton.addStretch(2)
        hBoxButton.addWidget(pm10Button)
        hBoxButton.addWidget(pm25Button)
        hBoxButton.addWidget(comTempButton)
        hBoxButton.addWidget(self.cb)

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

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(leftLayout)
        self.mainLayout.addLayout(rightLayout)

        self.timer = self.sc.new_timer(
            1000, [(self.update_Data, (), {})])
        self.timer.start()

        self.setLayout(self.mainLayout)
        self.show()

    def comboBoxYear(self):
        self.cb = QComboBox()
        self.cb.addItem('2008')
        self.cb.addItem('2009')
        self.cb.addItem('2010')
        self.cb.addItem('2011')
        self.cb.addItem('2012')
        self.cb.addItem('2013')
        self.cb.addItem('2014')
        self.cb.addItem('2015')
        self.cb.addItem('2016')
        self.cb.addItem('2017')
        self.cb.addItem('2018')
        self.cb.addItem('2019')
        self.cb.addItem('2020')
        self.cb.addItem('2021')

    def push_button_pm10(self):
        self.key = "pm10"
        self.draw_graph()
        self.textPM()

    def push_button_pm25(self):
        self.key = "pm25"
        self.draw_graph()
        self.textPM()

    def push_button_compareTemp(self):
        self.key = "temp"
        self.draw_graph()
        self.textPM()

    def draw_graph(self):
        if self.key == 'temp':
            getListDB = GetListDB(show.BME2)
            getListDB.getValue(int(self.cb.currentText()))
            self.sc.axes.cla()
            self.sc.axes.plot(getListDB.sortedListDB_X("개월"), getListDB.sortedListDB_Y("pm10 평균"), color='red')
            self.sc.axes.plot(getListDB.sortedListDB_X("개월"), getListDB.sortedListDB_Y("pm25 평균"), color='blue')
            self.sc.axes.set_xlabel("Month")
            self.sc.axes.set_ylabel("Red : Temp & Blue : Humi")
            self.sc.axes.grid()
            self.sc.draw()
        else :
            getListDB = GetListDB(show.PMS)
            self.sc.axes.cla()
            self.sc.axes.plot(getListDB.sortedListDB_X(self.key), getListDB.sortedListDB_Y(self.key))
            self.sc.axes.set_xlabel("ID")
            self.sc.axes.set_ylabel(self.key)
            self.sc.axes.grid()
            self.sc.draw()

    def textPM(self):
        self.tempAver = AverageValue(show.BME, "temp")
        self.humiAver = AverageValue(show.BME, "humi")

        self.tempText.setText("온도 : " + str(self.tempAver.AverValue()))
        self.humiText.setText("습도 : " + str(self.humiAver.AverValue()))

        if self.key == "pm10":
            self.pmText.setText("<PM10>\n좋음 : 0 ~ 30 \n보톰 : 31 ~ 80\n나쁨 : 81 ~ 150\n매우 나쁨 : 151이상")
        elif self.key == "pm25":
            self.pmText.setText("<PM2.5>\n좋음 : 0 ~ 15 \n보톰 : 15 ~ 35\n나쁨 : 36 ~ 75\n매우 나쁨 : 76이상")

        if self.key == "temp":
            self.nowPmText.clear()
        else:
            self.pmAver = AverageValue(show.PMS, self.key)
            self.comPM = ComparePm(self.pmAver.lastValue(), self.key)
            self.nowPmText.setText("현재 미세먼지 농도는 \n" + self.comPM.ComparePM() + "(" + str(self.pmAver.lastValue()) + ") 입니다.")

    def update_Data(self):
        importlib.reload(show)
        self.textPM()
        self.draw_graph()

if __name__=="__main__" :
   app = QApplication(sys.argv)
   main = Main()
   sys.exit(app.exec_())