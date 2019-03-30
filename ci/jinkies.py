import model

from zweeBasic import *

h = model.train()
for i in h.history:
    print(i)
    
    if i == "loss":
        TestLang.LOSS = h.history[i][-1]
    elif i == "val_loss":
        TestLang.VAL_LOSS = h.history[i][-1]
    elif i == "acc":
        TestLang.ACC = h.history[i][-1]
    elif i == "val_acc":
        TestLang.VAL_ACC = h.history[i][-1]
    elif i == "precision":
        TestLang.PRECISION = h.history[i][-1]
    elif i == "val_precision":
        TestLang.VAL_PRECISION = h.history[i][-1]
    elif i == "recall":
        TestLang.RECALL = h.history[i][-1]
    elif i == "val_recall":
        TestLang.VAL_RECALL = h.history[i][-1]
    
    print(h.history[i])
    import numpy
    print(type(h.history[i][-1]) == numpy.float32)
    print("length = " + str(len(h.history[i]))) 
    print()

model.predict()
from time import time
from pymongo import MongoClient
client = MongoClient('3.94.109.234')
db = client.ci
build_info = {"build_time" : int(time())}
def _convert(t):
    if type(t) == numpy.float32:
        return float(t)
    return t
for param in dir(TestLang):
    if param.isupper():
        build_info[param] = _convert(getattr(TestLang, param))
print(build_info) 
db.builds.insert(build_info)
import tests
