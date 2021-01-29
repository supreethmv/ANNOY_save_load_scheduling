import annoy_retrain
import random

for i in range(10000):
    f = open("annoy_database.txt",'w')
    f.write(str(random.random()))
    f.close()
    annoy_retrain.annoy_retrain_fun()          #comlplex operation