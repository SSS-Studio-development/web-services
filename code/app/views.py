from app import app
from flask import request
import requests as req
import bs4

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
