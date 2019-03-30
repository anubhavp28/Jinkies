import model

from zweeBasic import *

h = model.train()
for i in h.history:
    print(i)
    print(h.history[i])
    print("length = " + str(len(h.history[i]))) 
    print()

model.predict()
