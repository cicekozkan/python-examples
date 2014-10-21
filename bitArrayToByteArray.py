# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 10:35:56 2014

@author: cicek
"""
def bitArrayToByteArray(bl, sizeToTransfer):
    """bl: bit list"""
    i=0
    j=0
    t = bl[:]
    element = 0
    sendBuf = []  
    while (i<sizeToTransfer):
        element += t[i]<<j;
        j+=1
        if (j%8==0):            
            sendBuf.append(element) 
            j=0
            element = 0
        i += 1
    if j!=0:
        sendBuf.append(element)
    return sendBuf
                
		    
    
        










