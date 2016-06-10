from app import app
from flask import request
import requests as req
import bs4
from dateutil.parser import parse
from datetime import datetime

@app.route("/translate", methods=['POST'])
def trans():

    sentence = request.json['sentence']
    words = sentence.split()
    answer = []
    for word in words :
        res = req.get('http://www.phonemicchart.com/transcribe/?w='+word)
        soup = bs4.BeautifulSoup(res.text)
        ret = soup.center
        if ret:
            answer.append(ret.string)
        else :
            answer.append(word)

    return " ".join(answer)

@app.route("/date-translate", methods=['POST'])
def datetrans():
    try :
        date_str = request.json['date']
    except :
        return 'Error occured, date format not valid or date not passed'
    try :
        forma = request.json['format']
    except:
        return 'format not provided'
    try:
        date = parse(date_str)
    except :
        return 'new date format not valid'
    return datetime.strftime(date,forma)
