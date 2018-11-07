# import pandas as pd
import json
import io
import random
#data = pd.read_html('BANGDIEMTOANKHOAD14.xls')
#print (type(data))
# print (data[0])
# print (data[0][0])
# print (data[0][0][0])
# print (data[0][0][1])
# for i in range(0, 8):
#     print (data[0][i][0])

# for j in range(0, 56):
#     print (data[0][1][j])



#value2 = dict({"MSV":"B15DCCN503", "STT":"1", "IDSubject":"DDGD12", "TC":3, "CC":6, "KT": 7, "BT": 7, "TH":6, "Final": 8})
#print (value2)
#value1 = list([value2])
#print (value1)
# for j in range(0, 56):
#     for i in range (0,8):
#         value2[i] = data[0][i][j]
#     value1.append(value2)
# print (len(value1))
#
#

# value2 = list()
# for i in range(0,10):
#     value1 = dict({"MSV": "B15DCCN{}".format(503+i), "STT": i})
#     #value2.keys("STT") = i
#     print (value1)
#     value2.append(value1)
# print (value2)
# with io.open('data.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(value2, ensure_ascii=False))
#

semesters = ("Spring", "Summer", "Autumn")
subjects = ("idle1", "idle2", "idle3", "idle4", "idle6")
value = list()
value1 = dict()
value4 = dict()




for i in range(0, 100):
    value3 = dict()
    for item in subjects:
        value2 = dict({"TC": random.randint(2, 3), "CC": random.randint(4, 10), "TH": random.randint(3, 10),
                       "KT": random.randint(3, 10),
                       "BT": random.randint(5, 10), "Exam": random.randint(1, 10)})
        value3.update({item: value2})
    value4.update({"B15DCCN{}".format((503+i)): value3})

for semester in semesters:
    value1.update({semester: value4})

value.append(value1)
with io.open('point.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(value, ensure_ascii=False))


