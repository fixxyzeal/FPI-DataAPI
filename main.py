from flask import Flask
from flask import jsonify
from flask import request
from flask.wrappers import Response
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from werkzeug.wrappers import response
import bl.user 
load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('DB')
app.config['MONGO_URI'] = os.environ.get('DBCONNECTION')
mongo = PyMongo(app)

@app.route('/user', methods=['POST'])
def Authenticate():
  username = request.json['UserName']
  password = request.json['PassWord']
  return Response(bl.user.Authenticate(mongo,username,password),mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=False)