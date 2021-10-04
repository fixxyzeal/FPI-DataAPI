from bl.user import Authenticate
from bl.crypto import InsertHistory
import os
from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import PyMongo
load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('DB')
app.config['MONGO_URI'] = os.environ.get('DBCONNECTION')
mongo = PyMongo(app)


def test_Authenticate():
    assert len(Authenticate(mongo, "a", "abb")) == 2


def test_InsertHistory():
    assert InsertHistory(mongo, "EVX", 49, 3)
