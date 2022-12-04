from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os
import csv
import math


load_dotenv()

MongoURI = os.environ.get("MongoURI")

myclient = MongoClient(MongoURI, 27017)

db = myclient["AD"]
pms = db["pms"]
bme = db["bme"] 

PMS = [db.pms.find({"createdAt" : -1}).limit(10)]
print(db.pms.find({"createdAt" : -1}).limit(10))

PMS = []

for d, cnt in zip(db.pms.find().sort("createdAt", -1).limit(10), range(1, 11, 1)):  # sensors 데이터베이스의 가장 최근 값 10개를 뒤집어서 가져옴
    print(cnt)  # x축 좌표에는 카운트 값
    print(d['pm25'])  # y축 좌표에는 센서 값
    ls = {"pm25":int(d['pm25']), "pm10":int(d['pm10'])}
    PMS.append(ls)

print(PMS)    


#날짜 설정
end_date = "2021-05-31"

begin_date_time = datetime.strptime('2008-1-1', '%Y-%m-%d')

end_date_time = datetime.strptime(end_date, '%Y-%m-%d')

gap = (end_date_time - begin_date_time)*24
print(gap.days)

#측정기간 월별 평균 조회
m = 1
day = 1
temp = 0
humi = 0
temp_avg = 0.0
humi_avg = 0.0
BME = []
for d, cnt in zip(db.bme.find(), range(gap.days)):
    s = datetime.strptime(d['date'], '%Y-%m-%d %H:%M')

    if m == 13:
        m = 1

    if s.hour == 12 and s.month == m:
        if d['temp'][0] == '-':
            temp = temp + (-1) * float(d['temp'][1:])
        else:
            temp = temp + float(d['temp'])
        humi = humi + int(d['humi'])
        day += 1
    elif (day >= 28):
        m = m + 1
        temp_avg = round((float(temp) / day),3)
        humi_avg = round((float(humi) / day),3)
        ls2 = {"개월": m - 1, "temp 평균": temp_avg, "humi 평균": humi_avg}
        BME.append(ls2)
        day = 1

        temp = 0
        humi = 0
        temp_avg = 0.0
        humi_avg = 0.0
print(BME)







# PMS = [
#     {'pm25': '1', 'pm10': '2'},
#     {'pm25': '3', 'pm10': '7'},
#     {'pm25': '12', 'pm10': '12'},
#     {'pm25': '22', 'pm10': '58'},
#     {'pm25': '27', 'pm10': '76'},
#     {'pm25': '32', 'pm10': '90'},
#     {'pm25': '17', 'pm10': '112'},
#     {'pm25': '20', 'pm10': '156'},
#     {'pm25': '17', 'pm10': '138'},
#     {'pm25': '19', 'pm10': '120'}
# ]


#BME = [
#    {'temp': '2', 'humi': '1'},
#    {'temp': '3', 'humi': '2'},
#    {'temp': '4', 'humi': '3'},
#    {'temp': '5', 'humi': '3'},
#    {'temp': '6', 'humi': '3'},
#    {'temp': '7', 'humi': '3'},
#    {'temp': '7', 'humi': '3'},
#    {'temp': '7', 'humi': '3'},
#    {'temp': '7', 'humi': '3'},
#    {'temp': '7', 'humi': '3'},
#    {'temp': '7', 'humi': '3'}
# ]
