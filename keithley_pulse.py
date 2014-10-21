# -*- coding: utf-8 -*-
"""
Created on Wed May 28 16:57:56 2014

@author: cicek
"""
from pyvisa import visa
from time import sleep

keithley=visa.instrument("GPIB::5")

keithley.write(':SOUR:VOLT 3.3')
keithley.write(':SOUR:VOLT 5.0')
sleep(0.002)
keithley.write(':SOUR:VOLT 3.3')
