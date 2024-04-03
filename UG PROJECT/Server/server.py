from flask import Flask, request, jsonify
import util
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
@app.route('/get_country_name', methods = ['GET'])
def get_country_name():
    response = jsonify({
        'Country' : util.get_country_name()
    })
    response.headers.add('Access-control-allow-origin', '*')
    return response
@app.route('/predict', methods= ['POST'])
def predict():
    Country = request.form['Country']   
    H = int(request.form['H'])           
    constuction_year = int(request.form['constuction_year'])
    response = jsonify({
        'estimated_failure' : [util.get_estimated_failure(Country,H	,constuction_year)[0],util.get_estimated_failure(Country,H	,constuction_year)[1]]
    })
    print(constuction_year)
    response.headers.add('Access-control-allow-origin', '*')
    return response
if __name__ == "__main__":
    print("starting python flask server for dam failure prediction...")
    util.load_saved_art()
    app.run()
