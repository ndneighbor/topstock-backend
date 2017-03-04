from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)

@app.route('/Quote', methods = ['GET'])
def quote():
	bigDict = {}
	bigDict["Name"] = "Apple Inc"
	bigDict["Symbol"] = "AAPL"
	bigDict["LastPrice"] = 524.49
	bigDict["Change"] = 15.6
	bigDict["ChangePercent"] = 3.06549549018453
	bigDict["Timestamp"] = "Wed Oct 23 13:39:19 UTC-06:00 2013"
	bigDict["High"] = 52499
	bigDict["Low"] = 519.175
	bigDict["Open"] = 519.175
	return json.jsonify(bigDict)

@app.route('/Quote/Topfive', methods = ['GET'])
def topFive():
	bigDict = {};
	bigDict["one"] = "Apple Inc"
	bigDict["Symbol-one"] = "AAPL"
	bigDict["LastPrice-one"] = 524.49
	bigDict["two"] = "Apple Inc"
	bigDict["Symbol-two"] = "AAPL"
	bigDict["LastPrice-two"] = 524.49
	bigDict["three"] = "Apple Inc"
	bigDict["Symbol-three"] = "AAPL"
	bigDict["LastPrice-three"] = 524.49
	bigDict["four"] = "Apple Inc"
	bigDict["Symbol-four"] = "AAPL"
	bigDict["LastPrice-four"] = 524.49
	bigDict["five"] = "Apple Inc"
	bigDict["Symbol-five"] = "AAPL"
	bigDict["LastPrice-five"] = 524.49
	return json.jsonify(bigDict)

@app.route('/Quote/TopStock', methods = ['GET'])
def topStock():
	bigDict = {};
	bigDict["one"] = "Apple Inc"
	bigDict["Symbol-one"] = "AAPL"
	bigDict["LastPrice-one"] = 524.49
	return json.jsonify(bigDict)
	
if __name__ == '__main__':
    app.run()