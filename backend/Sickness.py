#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, re
from datetime import datetime, time

epoch = datetime.utcfromtimestamp(0)

class Sickness(object):
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
        sicknessDate = ""
        dataStarts = False
        timePattern = re.compile('24')
        for r in datarows:
            if r[0].startswith('Date'):
                sessionStartDate = r[1]
                dataStarts = True
                continue
            if dataStarts == True:
                date = self.convertToUnixTime(r[0])
                sicknessHours = float(r[1])
                data.append([date, sicknessHours])
        return data

    # increment date string of following format: 14.11.2015
    def incrementDate(self, d):
        dc = d.split('.')
        dc[0] = str(int(dc[0]) + 1)
        return ".".join(dc)

    def convertToUnixTime(self, t):
        d = datetime.strptime(t, '%Y-%m-%d')
        return (d - epoch).total_seconds() # * 1000.0

    def cleanDataOutfile(self, outfile, data):
        with open(outfile, 'w') as file:
            output = csv.writer(file, delimiter=",")
            output.writerows(data)
