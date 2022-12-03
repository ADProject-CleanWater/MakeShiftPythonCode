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
from PyQt5.QtGui import QPixmap

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
        self.tempText.setFixedSize(250, 100)

        self.humiText = QLineEdit()
        self.humiText.setReadOnly(True)
        self.humiText.setAlignment(Qt.AlignLeft)
        font = self.humiText.font()
        font.setFamily('Courier New')
        self.humiText.setFont(font)
        self.humiText.setStyleSheet('color:black;font-size:28px;')
        self.humiText.setFixedSize(250, 100)

        self.nowPmText = QTextEdit()
        self.nowPmText.setReadOnly(True)
        self.nowPmText.setAlignment(Qt.AlignLeft)
        font = self.nowPmText.font()
        font.setFamily('Courier New')
        self.nowPmText.setFont(font)
        self.nowPmText.setStyleSheet('color:black;font-size:20px;')
        self.nowPmText.setFixedSize(250, 100)

        self.pmText = QTextEdit()
        self.pmText.setReadOnly(True)
        self.pmText.setAlignment(Qt.AlignRight)
        font = self.pmText.font()
        font.setFamily('Courier New')
        self.pmText.setFont(font)
        self.pmText.setStyleSheet('color:black;font-size:20px;')
        self.pmText.setFixedSize(250, 150)
        
        self.image = QLabel()
        self.image.setAlignment(Qt.AlignRight)
        self.image.setFixedSize(250, 250)

        self.textPM()

        pm10Button = QPushButton('PM10')
        pm10Button.clicked.connect(self.push_button_pm10)
        pm25Button = QPushButton('PM25')
        pm25Button.clicked.connect(self.push_button_pm25)
        comTempButton = QPushButton('Temp')
        comTempButton.clicked.connect(self.push_button_compareTemp)

        hBoxButton = QHBoxLayout()
        hBoxButton.addStretch(2)
        hBoxButton.addWidget(pm10Button)
        hBoxButton.addWidget(pm25Button)
        hBoxButton.addWidget(comTempButton)

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
        rightLayout.addStretch(1)
        rightLayout.addWidget(self.image)
        rightLayout.addLayout(hBoxButton)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        self.timer = self.sc.new_timer(
            100, [(self.update_Data, (), {})])
        self.timer.start()

        self.setLayout(mainLayout)
        self.show()

    def push_button_pm10(self):
        self.key = "pm10"
        self.draw_graph()
        self.textPM()

    def push_button_pm25(self):
        self.key = "pm25"
        self.draw_graph()
        self.textPM()

    def draw_graph(self):
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
        self.pmAver = AverageValue(show.PMS, self.key)
        self.comPM = ComparePm(self.pmAver.lastValue(), self.key)

        self.tempText.setText("온도 : " + str(self.tempAver.AverValue()))
        self.humiText.setText("습도 : " + str(self.humiAver.AverValue()))
        self.nowPmText.setText("현재 미세먼지 농도는 \n" + self.comPM.ComparePM() + "(" + str(self.pmAver.lastValue()) + ") 입니다.")
        if self.key == "pm10" :
            self.pmText.setText("<PM10>\n좋음 : 0 ~ 30 \n보톰 : 31 ~ 80\n나쁨 : 81 ~ 150\n매우 나쁨 : 151이상")
        elif self.key == "pm25" :
            self.pmText.setText("<PM2.5>\n좋음 : 0 ~ 15 \n보톰 : 15 ~ 35\n나쁨 : 36 ~ 75\n매우 나쁨 : 76이상")
            
        if self.comPM.ComparePM() == "좋음":
            image_update = "air_01.jpg"
        elif self.comPM.ComparePM() == "보통":
            image_update = "air_02.jpg"
        elif self.comPM.ComparePM() == "나쁨":
            image_update = "air_03.jpg"
        elif self.comPM.ComparePM() == "매우 나쁨":
            image_update = "air_04.jpg"
            
        self.image.setPixmap(QPixmap(image_update))

    def push_button_compareTemp(self):
        print("PUSH")

    def update_Data(self):
        importlib.reload(show)
        self.textPM()
        self.draw_graph()

if __name__=="__main__" :
   app = QApplication(sys.argv)
   main = Main()
   sys.exit(app.exec_())
