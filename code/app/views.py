
# -*- coding: utf-8 -*-
from app import app
from flask import request
import requests as req
import bs4
import pickle
from dateutil.parser import parse
from datetime import datetime

# -*- coding: utf-8 -*-

word_list = pickle.load( open( "word_list.p", "rb" ) )

translatekey = 'trnsl.1.1.20160620T044235Z.009e3fdaf079e045.51ec20ede6d14038c2cb193de1f8891c28dfc749'

# -*- coding: utf-8 -*-

@app.route("/phonetic-trans", methods=['POST'])
def phonetictrans():

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

# -*- coding: utf-8 -*-

@app.route("/phonetic-translive", methods=['POST'])
def phonetictranslive():

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

# -*- coding: utf-8 -*-

@app.route("/language-translive", methods=['POST'])
def languagetranslive():
    try:
        sentence = request.json['sentence']
    except:
        return "sentence parameter not passed"
    try :
        fromlang = request.json['from-language']
    except:
        return "en"
    try :
        tolang = request.json['to-language']
    except:
        return "to language not passed"

        
    res = req.get('https://translate.yandex.net/api/v1.5/tr/translate?key='+translatekey+'&text='+sentence+'&lang='+fromlang+'-'+tolang+'&format=plain&options=0');
    soup = bs4.BeautifulSoup(res.text)
    ret = soup.text
    return ret;

# -*- coding: utf-8 -*-

@app.route("/test", methods=['GET'])
def test():
    return "some test string"
