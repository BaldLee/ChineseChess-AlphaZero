import os
import json

path = os.getcwd() + "/play_data"
target = os.getcwd() + "/target"
files = os.listdir(path)

# for item in files:

for item in files:
    f = open(path + '/' + item, "rt")
    j = json.load(f)
    datas = []
    data = []
    for i in j:
        if i[0] == 'r':
            data = []
            datas.append(data)
        data.append(i)
    for idx, d in enumerate(datas):
        newname = target+'/'+item.split('.')[0]+'-'+str(idx)+".json"
        with open(newname, "w") as fout:
            json.dump(d, fout)
