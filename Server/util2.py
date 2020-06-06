import json
import pickle
import numpy as np



__locations = None
__data_columns = None
__model = None



def get_estimated_price(location,sq_mt_built,n_rooms,n_bathrooms):
    try:
        loc_index = __data_columns.index(location.lower()) # From a list, we can get the index by simply using .index()
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sq_mt_built
    x[1] = n_rooms
    x[2] = n_bathrooms
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0]) # this is how we call our model. x is the input in the form of a 2D array

def get_location_names():
    return __locations

def load_saved_artifacts(): # this function takes both artifact files and saves the info into global variables
    print("loading saved artifacts...start")

    global __data_columns
    global __locations

    with open("./artifacts/columns_Nooutliers.json", "r") as f: # with ./ we go one folder up
        __data_columns = json.load(f)["data_columns"] # We read our json file an import the data and set our variable (list)
        __locations = __data_columns[3:] # The locations start at index 3

    global __model  # Do not forget to define __model as a global variable

    with open("./artifacts/Madrid_home_price_mode_Nooutliers.pickle", "rb") as f: # Since is a binary model we will use rb. A
    # binary regression estimates a relationship between one or more explanatory variables and a single output binary variable
        __model  = pickle.load(f)

    print("loading saved artifacts...done")

if __name__== "__main__":
    load_saved_artifacts()
    get_location_names()
    print(get_estimated_price("Chamartín", 119, 3, 2), "euros")
