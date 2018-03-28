# -*- coding: UTF-8 -*-
import os
import datetime
from datetime import timedelta
# ref: http://sqlblog.com/blogs/louis_davidson/archive/2010/02/04/creating-and-using-a-time-not-date-table-dimension.aspx
start = datetime.datetime.strptime("00:00", "%H:%M")
file = open('../dimentions/d_time.csv', 'w')
index = 0

def get_time_proxy(arg1):
    return bytes(arg1)

def get_time_24hour_key(arg1):
    return arg1.strftime("%H:%M")

def get_hour_of_day_24(arg1):
    return bytes(int(arg1.strftime("%H")))

def get_hour_of_day_12(arg1):
    return bytes(int(arg1.strftime("%H"))%12)

def get_am_pm(arg1):
    return 'AM' if int(arg1.strftime("%H")) < 11 else  'PM'

def get_minute_of_hour(arg1):
    return  bytes(int(arg1.strftime("%M"))) 

def get_half_hour(arg1):
    return bytes(((arg1/30) % 2) + 1)

def get_half_hour_of_day(arg1):
    return  bytes((arg1/30) + 1)

def  get_quarter_hour(arg1):
    return  bytes(((arg1/15) % 4) + 1)

def get_quarter_hour_of_day(arg1):
    return bytes((arg1/15) + 1)

def get_string_representation_24(arg1):
    return arg1.strftime("%H:%M")

def get_string_representation_12 (arg1):
    return arg1.strftime("%H:%M") if int(arg1.strftime("%H")) < 12 else  (arg1 - timedelta(hours = 12)).strftime("%H:%M")

flag = start
while index  < 1440:
    file.write( get_time_proxy(index) + ' '+ get_time_24hour_key(flag) + ' '+ get_hour_of_day_24(flag) + ' '+ get_hour_of_day_12(flag) + ' '+ get_am_pm(flag) +  ' ' + get_minute_of_hour(flag) +  ' '  +  get_half_hour(index)  + ' '  +  get_half_hour_of_day(index)+ ' ' + get_quarter_hour(index)  +' ' + get_quarter_hour_of_day(index)+  ' ' +  get_string_representation_24(flag) +  ' ' +  get_string_representation_12(flag) +"\n")
    index  =  index + 1
    flag =  start  + timedelta(minutes  =  index)
file.close()