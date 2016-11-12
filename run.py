#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

import Sickness
import CO2MeetingRoom
import Energy1stFloor
import Energy2ndFloor
import Energy3rdFloor
import EnergyOther

'''
sick = Sickness.Sickness()
datafile = "sickness.csv"
data = sick.parseDataFile(datafile)

data2 = np.asarray(data)

workerNr = 1
plt.plot(data2[:,1][workerNr:-1:10])
plt.show()
'''
'''
co2 = CO2MeetingRoom.CO2MeetingRoom()
datafile = "IAQ_CO2_meeting_room.csv"
data = co2.parseDataFile(datafile)
'''
'''
energy = Energy1stFloor.Energy1stFloor()
datafile = "energy3rdFloor.csv"
data = energy.parseDataFile(datafile)
'''

energyO = EnergyOther.EnergyOther()
datafile = "energyOther.csv"
data = energyO.parseDataFile(datafile)

data2 = np.asarray(data)



plt.plot(data2)
plt.show()



#print data
