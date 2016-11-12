#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, re
from datetime import datetime, time

epoch = datetime.utcfromtimestamp(0)

class CO2MeetingRoom(object):
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
            if r[0].startswith('Sensor_ID'):
                dataStarts = True
                continue
            if dataStarts == True:
                sensor_id = int(r[0])
                d = r[1] + '-' + r[2].zfill(8)
                date = self.convertToUnixTime(d)
                co2 = float(r[3])
                sicknessHours = float(r[1])
                data.append([sensor_id, date, co2])
        return data


    def incrementDate(self, d):
        dc = d.split('.')
        dc[0] = str(int(dc[0]) + 1)
        return ".".join(dc)

    ## time conversion does not work
    ## http://stackoverflow.com/questions/7588511/format-a-datetime-into-a-string-with-milliseconds
    def convertToUnixTime(self, t):
        d = datetime.strptime(t, '%Y-%m-%d-%H:%M:%S.%f')[:-3] # problem
        return (d - epoch).total_seconds() # * 1000.0

    def cleanDataOutfile(self, outfile, data):
        with open(outfile, 'w') as file:
            output = csv.writer(file, delimiter=",")
            output.writerows(data)
