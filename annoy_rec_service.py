#import retrain
import pickle
import time
import os
from annoy import AnnoyIndex

#Load the model
for i in range(1000):
    model = AnnoyIndex(1,'angular')
    model.load('annoy_model.pkl')
    print(model.get_nns_by_item(0,1))
    print(model)
    #time.sleep(0.1)