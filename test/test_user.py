from bl.user import Authenticate
import os
from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import PyMongo
load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('DB')
app.config['MONGO_URI'] = os.environ.get('DBCONNECTION')
mongo = PyMongo(app)

def test_getsetdata():
    assert  len(Authenticate(mongo,"a","Zeallyfixxy5!")) == 2