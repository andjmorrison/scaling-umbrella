from dotenv import load_dotenv
from os import getenv
from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
import numpy as np

# Load environment variables
load_dotenv()

# Create an instance of Flask
app = Flask(__name__)

# Get the connection string for the database
app.config['MONGO_URI'] = getenv('MONGO_URI', '')

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # open connection // flask-pymongo mannages connections
    mongo = PyMongo(app)

    # Find one record of data from the mongo database // exclude id field
    destination_data = mongo.db.vacation.find({}, {'_id': False})

    # construct array 
    destination_data = [x for x in destination_data]

    # get random index
    random_select = np.random.randint(low=0, high=3)

    # use random index to select a doc
    destination_data = destination_data[random_select]

    # Return template and data
    return render_template("index.html", vacation=destination_data)

@app.route('/data')
def my_data():

    # open connection
    mongo = PyMongo(app)

    # pull down doc from mongoDB
    my_query = mongo.db.vacation.find({}, {'_id': False})

    # construct array
    my_data = [x for x in my_query]

    # return array
    return jsonify(my_data)

if __name__ == "__main__":
    app.run(debug=True)
