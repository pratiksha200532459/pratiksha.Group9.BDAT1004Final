from flask import Flask,render_template,sessions, request
from pymongo import MongoClient
from flask_pymongo import pymongo
from bson import json_util
import json
import certifi


app = Flask(__name__)

client = MongoClient('mongodb+srv://pratikshasm:Bangalore123@weather.r2lo4vz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client['weather']
collection = db['weather']

@app.route('/')
def getdata():
    global datas
    datas = list(collection.find({}))
    return json.dumps(datas, default=json_util.default)
def index():
    return render_template('index.html', datas=datas)