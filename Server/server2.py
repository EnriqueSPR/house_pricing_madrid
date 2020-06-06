from flask import Flask, request, jsonify
import util2

app = Flask(__name__)

@app.route("/get_location_names") # We need two routines: One for the locations(in util file)
def get_location_names(): # this will return all the locations
    response = jsonify({"locations": util2.get_location_names()}) # Returning a response that contain the locations
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route("/predict_home_price", methods=["POST"]) # We need two routines: One for the locations(in util file)
def predict_home_price():
    sq_mt_built = float(request.form["sq_mt_built"])
    location = str(request.form["location"])
    n_rooms = float(request.form["n_rooms"])
    n_bathrooms = float(request.form["n_bathrooms"])

    response = jsonify({"EstimatedPrice": util2.get_estimated_price(location, sq_mt_built, n_rooms, n_bathrooms)})

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__=="__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util2.load_saved_artifacts()
    app.run()
