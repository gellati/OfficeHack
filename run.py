#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

import Sickness

sick = Sickness.Sickness()
#datafile = r"\'2 sickness_data.csv\'"
datafile = "sickness.csv"

data = sick.parseDataFile(datafile)
data2 = np.asarray(data)

#plt.plot(data2)
#plt.show()

workerNr = 1
plt.plot(data2[:,1][workerNr:-1:10])
plt.show()

#print data
