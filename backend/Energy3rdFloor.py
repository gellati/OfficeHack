#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, re, json, bisect
from datetime import datetime, time

epoch = datetime.utcfromtimestamp(0)

timeData = []
timeDates = []

class Energy3rdFloor(object):
    def __init__(self): pass

    def readDataFile(self, filename):
        file = filename
        datarows = []
        with open(file, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                datarows.append(row)
        return datarows

    def parseDataFile(self, filename):
        datarows = self.readDataFile(filename)
        dataStarts = False
        data = []
        for r in datarows:
            if r[0].startswith('Date'):
                dataStarts = True
                continue
            if dataStarts == True:
                d = r[0] + "-" + r[1]
                date = self.convertToDate(d)
                lighting3A = float(r[2])
                lighting3B = float(r[3])
                lighting3C = float(r[4])
                sockets3A = float(r[5])
                sockets3B = float(r[6])
                sockets3C = float(r[7])
                total3A = float(r[8])
                total3B = float(r[9])
                total3C = float(r[10])

                data.append([date, lighting3A, lighting3B, lighting3C, sockets3A, sockets3B, sockets3C, total3A, total3B, total3C])
                timeDates.append(date)
                timeData.append([lighting3A, lighting3B, lighting3C, sockets3A, sockets3B, sockets3C, total3A, total3B, total3C])
        return data

    def getTimeData(self, time):
        tdata = self.nearestTimeDataValue(time)
        return tdata

    def nearestTimeDataValue(self, queryDate):
        position = bisect.bisect_left(timeDates, queryDate)
        return timeData[position]

    def incrementDate(self, d):
        dc = d.split('.')
        dc[0] = str(int(dc[0]) + 1)
        return ".".join(dc)

    def convertToDate(self, t):
        d = datetime.strptime(t, '%Y-%m-%d-%H:%M:%S')
        return d

    def convertToUnixTime(self, t):
        d = datetime.strptime(t, '%Y-%m-%d-%H:%M:%S')
        return (d - epoch).total_seconds() # * 1000.0

    def cleanDataOutfile(self, outfile, data):
        with open(outfile, 'w') as file:
            output = csv.writer(file, delimiter=",")
            output.writerows(data)
