import os
import json

path = os.getcwd() + "/play_data"
target = os.getcwd() + "/target"
files = os.listdir(path)

folder = os.path.exists(target)
if not folder:          
    os.makedirs(path)
    print(f"create folder \"target/\"")

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
    if len(datas) > 1:
        print(f"file: {item} is wrong")
        for idx, d in enumerate(datas):
            newname = target+'/'+item.split('.json')[0]+'-'+str(idx)+".json"
            with open(newname, "w") as fout:
                json.dump(d, fout)
    else:
        with open(target+'/'+item, "w") as fout:
            json.dump(datas[0], fout)