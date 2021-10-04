from flask import Flask
from flask import jsonify
from flask import request
from flask.wrappers import Response
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

import bl.user
import bl.crypto
load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('DB')
app.config['MONGO_URI'] = os.environ.get('DBCONNECTION')
mongo = PyMongo(app)


@app.route("/")
def index() -> str:
    return jsonify({"message": "FPI Data API Service"})


@app.route('/user', methods=['POST'])
def Authenticate():
    username = request.json['UserName']
    password = request.json['PassWord']
    return Response(bl.user.Authenticate(mongo, username, password), mimetype='application/json')


@app.route('/insertcryptohistory', methods=['POST'])
def InsertCryptoHistory():
    cryptoname = request.json['CryptoName']
    amt = request.json['Amt']
    rate = request.json['Rate']
    return jsonify({"ID": str(bl.crypto.InsertHistory(mongo, cryptoname, amt, rate))})


if __name__ == '__main__':
    app.run(debug=False)
