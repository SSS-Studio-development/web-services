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

word_list = pickle.load( open( "word_list.p", "rb" ) )

@app.route("/translate", methods=['POST'])
def trans():

    sentence = request.json['sentence']
    words = sentence.split()
    answer = []
    for word in words :

        word = word.lower()
        if word in word_list:
            answer.append(word_list[word])
        else :
            answer.append(word)


    return " ".join(answer)

@app.route("/translatelive", methods=['POST'])
def translive():

    sentence = request.json['sentence']
    words = sentence.split()
    answer = []
    for word in words :

        word = word.lower()
        res = req.get('http://www.phonemicchart.com/transcribe/?w='+word)
        soup = bs4.BeautifulSoup(res.text)
        ret = soup.center
        if ret:
            answer.append(ret.string)
        else :
            answer.append(word)


    return " ".join(answer)


@app.route("/test", methods=['GET'])
def test():
    return "some test string"
