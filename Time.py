# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 10:15:25 2014

@author: asus
"""

class Time(object):
    """Represents the time of the day
    attributes: hour, minutes, seconds"""
    def __init__(self,hour=0,minutes=0,seconds=0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minutes, self.seconds)
    def __add__(self,other):
        if isinstance(other,Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self,other):
        return self.__add__(other)
    def print_time(self):
        """Prints the time"""
        print '%.2d:%.2d:%.2d' % (self.hour, self.minutes, self.seconds)
    def time_to_int(self):
        """Converts time to seconds"""
        minutes = self.hour * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds
    def increment(self,seconds):
        """adds given number of seconds to a time object"""
        seconds += self.time_to_int()
        return int_to_time(seconds)  
    def is_after(self,other):
        return self.time_to_int() > other.time_to_int()
    def add_time(self, other):
        """adds given time object"""
        assert valid_time(self) and valid_time(other)
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    def print_attributes(self):
        for attr in self.__dict__:
            print attr, getattr(self,attr)
        
def valid_time(time):
    if time.hour < 0 or time.minutes < 0 or time.seconds < 0:
        return False
    if time.minutes >= 60 or time.seconds >= 60:
        return False
    return True
    

        
def int_to_time(seconds):
    time = Time()
    minutes, time.seconds = divmod(seconds, 60)
    time.hour, time.minutes = divmod(minutes, 60)
    time.hour = time.hour % 24
    return time
    

        
def increment_pure(time,seconds):        
    """adds given number of seconds to the time defined by input object
    and returns a new time object"""
    res = Time()
    res.hour = time.hour
    res.minutes = time.minutes    
    res.seconds = time.seconds + seconds
    
    if res.seconds > 59:
        res.minutes += (res.seconds)//60
        res.seconds = (res.seconds)%60
    
    if res.minutes > 59:
        res.hour += (res.minutes)//60
        res.minutes = (res.minutes)%60
        
    return res
    
def increment_2(time,seconds):
    """modified version of increment that uses time_to_int and int_to_time
    function"""
    return int_to_time(time_to_int(time) + seconds)