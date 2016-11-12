#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from datetime import datetime, date, time
from Sickness import Sickness
from Energy1stFloor import Energy1stFloor
from Energy2ndFloor import Energy2ndFloor
from Energy3rdFloor import Energy3rdFloor

e1f = Energy1stFloor()
e2f = Energy2ndFloor()
e3f = Energy3rdFloor()


app = Flask(__name__)
CORS(app)

sick = Sickness()

@app.route('/', methods=['GET'])
def HelloWorld():
    return jsonify({'Hello': 'world'})

@app.route('/sickness/query', methods=['GET'])
def getSickData():
    return 'sick'

@app.route('/energy/floor/1/query')
def getEnergy1stData():
    timeString = request.args.get('time')
    d = timeStringToDate(timeString)
    energyTimeData = e1f.parseDataFile('../data/energy1stFloor.csv')
    timeData = e1f.getTimeData(d)
    return jsonify({'lighting1A': timeData[0],
                    'lighting1B': timeData[1],
                    'lighting1C': timeData[2],
                    'sockets1A': timeData[3],
                    'sockets1B': timeData[4],
                    'sockets1C': timeData[5],
                    'total1A': timeData[6],
                    'total1B': timeData[7],
                    'total1C': timeData[8]})

@app.route('/energy/floor/2/query')
def getEnergy2ndData():
    timeString = request.args.get('time')
    d = timeStringToDate(timeString)
    energyTimeData = e1f.parseDataFile('../data/energy2ndFloor.csv')
    timeData = e1f.getTimeData(d)
    return jsonify({'lighting2A': timeData[0],
                    'lighting2B': timeData[1],
                    'lighting2C': timeData[2],
                    'sockets2A': timeData[3],
                    'sockets2B': timeData[4],
                    'sockets2C': timeData[5],
                    'total2A': timeData[6],
                    'total2B': timeData[7],
                    'total2C': timeData[8]})

@app.route('/energy/floor/3/query')
def getEnergy3rdData():
    timeString = request.args.get('time')
    d = timeStringToDate(timeString)
    energyTimeData = e1f.parseDataFile('../data/energy3rdFloor.csv')
    timeData = e1f.getTimeData(d)
    return jsonify({'lighting3A': timeData[0],
                    'lighting3B': timeData[1],
                    'lighting3C': timeData[2],
                    'sockets3A': timeData[3],
                    'sockets3B': timeData[4],
                    'sockets3C': timeData[5],
                    'total3A': timeData[6],
                    'total3B': timeData[7],
                    'total3C': timeData[8]})



def timeStringToDate(timestring):
    #  print (args) # For debugging
    try:
        ddate = datetime.strptime(timestring, '%Y-%m-%d')
        return ddate

    except Exception as e:
      return {'error': str(e)}


if __name__ == '__main__':
    app.run(debug = True,
            port = int(os.getenv('PORT', 8080)),
            host = '0.0.0.0')
