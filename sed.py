# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 09:51:22 2014

@author: cicek
"""

def sed(pattern, new, file1, file2):
    try:
        f1=open(file1, 'r')
        f2=open(file2, 'w')
        for line in f1:
            if pattern in line:
                newline=line.replace(pattern, new)
                f2.write(newline)
            else:
                f2.write(line)     
        f1.close()
        f2.close()
    except:
        print 'Something went wrong'
            