# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:59:11 2014

@author: cicek
"""
import urllib

zipcode=raw_input('enter the zip code: ')
url = 'http://www.uszip.com/zip/' + zipcode 
conn = urllib.urlopen(url)
for line in conn:
    if '<h2><strong>' in line:
        city=line.partition('<h2><strong>')[2].partition(' <')[0]
        state=line.partition('<a')[2].partition('>')[2].partition('</a>')[0]
        print city + state
    if 'Total population' in line:
        print line.partition('Total population</dt><dd>')[2].partition('<')[0]
        