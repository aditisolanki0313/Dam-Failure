import json
import pickle
import numpy as np
__Country = None
__data_columns = None
__model = None

def get_estimated_failure(Country,H	,constuction_year):
    try:
        Con_index = __data_columns.index(Country.lower())
    except:
        Con_index = -1
    
    x_input = np.zeros(len(__data_columns))
    x_input[0] = H
    x_input[1] = constuction_year

    if Con_index >=0:
        x_input[Con_index] = 1
    return round(__model.predict([x_input])[0],2)

def load_saved_art():
    print("loading saved art...start")
    global __data_columns
    global __Country

    with open("server/art/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __Country = __data_columns
    global __model
    if __model is None:
        with open("server/art/dam_failure_model.pickle", 'rb') as f:
            __model = pickle.load(f)
        print("loading saved art...done")

def get_country_name():
    return __Country

def get_data_columns():
    return __data_columns

if __name__=="__main__":
    load_saved_art()
    print(get_country_name())
    print(get_estimated_failure('India',18,1995))
