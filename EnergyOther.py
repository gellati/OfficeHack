#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, csv, re
from datetime import datetime, time

epoch = datetime.utcfromtimestamp(0)

class EnergyOther(object):
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
                d = r[0] + "-" + r[1].zfill(8)
                date = self.convertToUnixTime(d)
                parkingGarage = float(r[2])
                realEstateElectricity = float(r[3])
                waterChiller = float(r[4])
                totalBuildingElectricity = float(r[5])
                data.append([date, parkingGarage, realEstateElectricity, waterChiller, totalBuildingElectricity])
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
