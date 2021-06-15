from flask import Flask, jsonify
import time
from random import randrange


app = Flask(__name__)

"""
custom query function
"""
@app.route('/index/<string:query>')
def process_request(query):
    
    result={
        "query" : query,
        "request" : "index page",
        #"host IP" : "10.0.0.0:5000"
    }
    return jsonify(result)

"""
Simple function returns tax certificate status
"""
@app.route('/getTaxCertificate/')
def certReturn():
    start = time.time()
    end = time.time()
    eTime = end - start
    rand1=randrange(100000, 300000)
    rand2=randrange(100000, 300000)
    strIncidentNumber = str(rand1) + "-" + str(rand2)
    randNum=randrange(0,6)
    if (randNum >= 5):
        return "Creating your incident is taking longer than usual."
    else:
        return "Your incident has been created successfully. Incident ID :" + strIncidentNumber + ".​ What else can I help you with?"

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3449)