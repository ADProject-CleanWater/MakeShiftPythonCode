from pymongo import MongoClient

myclient = MongoClient("mongodb://3.34.50.139:27017/", 27017)

db = myclient["testsensor"]
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


BME = [
    {'temp': '2', 'humi': '1'},
    {'temp': '3', 'humi': '2'},
    {'temp': '4', 'humi': '3'},
    {'temp': '5', 'humi': '3'},
    {'temp': '6', 'humi': '3'},
    {'temp': '7', 'humi': '3'},
    {'temp': '7', 'humi': '3'},
    {'temp': '7', 'humi': '3'},
    {'temp': '7', 'humi': '3'},
    {'temp': '7', 'humi': '3'},
    {'temp': '7', 'humi': '3'}
]