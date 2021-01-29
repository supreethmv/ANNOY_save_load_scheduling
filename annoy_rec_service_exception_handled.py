#import retrain
import pickle
import time
import os
from annoy import AnnoyIndex

miss = 0
#Load the model
for i in range(1000):
    try:
        model = AnnoyIndex(1,'angular')
        model.load('annoy_model.pkl')
        #print(model.get_nns_by_item(0,1))
        #print(model)
    except Exception as e:
        print(e)
        miss+=1
        pass
miss_rate = miss / 1000
print("Miss Rate =",miss_rate)