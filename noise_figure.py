# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 11:15:19 2014

Noise figure test without a noise source. 
There are two sections in this test: 1) Connect an RF source to the input
of DUT and measure the gain
2) Terminate the input of DUT with a 50 ohm and measure the output noise

@author: cicek
"""

from pyvisa import visa

def PromptUser():
    """prompt user to get necessary information: GPIB addresses etc."""
    addr = raw_input('Enter GPIB address of Spectrum Analyzer: ')    
    if (addr < '0'):
        print("GPIB addr cannot be smaller than 0")
        return None
    else:
        addr = "GPIB::" + addr    
        spa = visa.instrument(addr)
    
    addr = raw_input('Enter GPIB address of RF Signal Source: ')    
    if (addr < '0'):
        print("GPIB addr cannot be smaller than 0")
        return None
    else:
        addr = "GPIB::" + addr
        rf = visa.instrument(addr)
        
    addr = raw_input('Enter GPIB address of Power Supply: ')    
    if (addr < '0'):
        print("GPIB addr cannot be smaller than 0")
        return None
    else:
        addr = "GPIB::" + addr()
        ps = visa.instrument(addr)
        
def InitializeInstruments():
    """Initialize instruments"""
        
