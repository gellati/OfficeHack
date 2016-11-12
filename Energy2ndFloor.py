#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, re
from datetime import datetime, time

epoch = datetime.utcfromtimestamp(0)

class Energy1stFloor(object):
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
        data = []
        dataStarts = False

        for r in datarows:
            if r[0].startswith('Date'):
                dataStarts = True
                continue
            if dataStarts == True:
                d = r[0] + "-" + r[1]
                date = self.convertToUnixTime(d)
                lighting1A = float(r[2])
                lighting1B = float(r[3])
                lighting1C = float(r[4])
                sockets1A = float(r[5])
                sockets1B = float(r[6])
                sockets1C = float(r[7])
                total1A = float(r[8])
                total1B = float(r[9])
                total1C = float(r[10])                
                data.append([date, lighting1A, lighting1B, lighting1C, sockets1A, sockets1B, sockets1C, total1A, total1B, total1C])
        return data


    def incrementDate(self, d):
        dc = d.split('.')
        dc[0] = str(int(dc[0]) + 1)
        return ".".join(dc)

    def convertToUnixTime(self, t):
        d = datetime.strptime(t, '%Y-%m-%d-%H:%M:%S')
        return (d - epoch).total_seconds() # * 1000.0

    def cleanDataOutfile(self, outfile, data):
        with open(outfile, 'w') as file:
            output = csv.writer(file, delimiter=",")
            output.writerows(data)
