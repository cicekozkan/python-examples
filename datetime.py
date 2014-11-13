# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 19:13:58 2014

@author: ocicek
"""

import datetime

def print_today():
    today=datetime.date.today()
    print "Year=%d, month=%d, day=%d" %(today.year, today.month, today.day)
    
def find_age_birthday(year, month, day):
    """takes a birthday as input and prints the user’s age and the number of
    days, hours, minutes and seconds until their next birthday."""
    today=datetime.date.today()
    age = abs(today.year - year)
    print 'Age=%d'%age
    next_birthday = datetime.date(today.year, month, day)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year = today.year + 1)
    time_to_birthday = abs(next_birthday - today)
    #print "Next birthday is %d days, %d hours, %dminutes and %d seconds later"\
    print "Next birthday is %d days later"\
    %(time_to_birthday.days)
    
def double_day(year1,month1,day1,year2,month2,day2):
    """For two people born on different days, there is a day when one is 
    twice as old as the other. That’s their Double Day. Write a program 
    that takes two birthdays and computes their Double Day."""
    bd1=datetime.date(year1,month1,day1)
    bd2=datetime.date(year2,month2,day2)
    dif = abs(bd1-bd2)
    if bd1 < bd2:
        dd = bd2 + dif
    else: 
        dd = bd1 + dif

    print 'the double day is %d/%d/%d'%(dd.year, dd.month, dd.day)
    
def n_day(n,year1,month1,day1,year2,month2,day2):
    """the more general version of double_day that computes the day when one
    person is n times older than the other."""
    bd1=datetime.date(year1,month1,day1)
    bd2=datetime.date(year2,month2,day2)
    dif = abs(bd1-bd2)
    if bd1 < bd2:
        nd = bd2 + dif/((n-1)*365)
    else: 
        nd = bd1 + dif/((n-1)*365)
    
    print 'the n day is %d/%d/%d'%(nd.year, nd.month, nd.day)