import time
import pickle
from annoy import AnnoyIndex

def annoy_retrain_fun():
    f = open("annoy_database.txt",'r')
    #time.sleep(1)           #comlplex operation
    model_data = float(f.read())
    f.close()
    #print(type(model))
    #print(model_data)
    tree = AnnoyIndex(1, 'angular')
    tree.add_item(0,[model_data])
    tree.build(1)
    save_success_flag = 0
    while not save_success_flag:
        try:
            tree.save('annoy_model.pkl')
            save_success_flag = 1
        except Exception as e:
            print(e)
            pass