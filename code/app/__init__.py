from flask import Flask
from flask import request
from flask_cors import CORS
from flask import request
import requests as req
import bs4
import pickle
from dateutil.parser import parse
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


from app import views
