# -*- coding: UTF-8 -*-
import os
import datetime
from datetime import timedelta
# date_proxy_key     date_key1      date_key2           year      month   day      quarter_name    day_name_of_week
# 20000101              2000_01_01     2000-01-01         2000       01           01             Q1                           Sunday
start = '2000 01 01'
end = '2030 12 31'
flag = start
file = open('../dimentions/d_date.csv', 'w')

def get_date_proxy_key(arg1):
    return arg1.strftime("%Y%m%d")

def get_date_key1(arg1):
    return arg1.strftime("%Y_%m_%d")

def get_date_key2(arg1):
    return arg1.strftime("%Y-%m-%d")

def get_year(arg1):
    return arg1.strftime("%Y")

def get_month(arg1):
    return arg1.strftime("%m")

def get_day(arg1):
    return arg1.strftime("%d")

def get_quarter_name(arg1):
    month =arg1.strftime("%m")
    if month in ['01', '02', '03']:
    	return 'Q1'
    elif month in ['04', '05', '06']:
    	return  'Q2'
    elif month in ['07', '08', '09']:
               return 'Q3'
    else:
               return 'Q4'

def get_day_name_of_week(arg1):
    return arg1.strftime("%A")	

while flag != end:
    flag = datetime.datetime.strptime(flag, "%Y %m %d")
    file.write(get_date_proxy_key (flag)+ ' ' + get_date_key1(flag) + ' ' + get_date_key2(flag) + ' '  + get_year(flag)  + ' ' + get_month(flag) + ' ' +  get_day(flag) + ' '  + get_quarter_name(flag) + ' ' + get_day_name_of_week(flag)  +"\n")
    flag = (flag + timedelta(days = 1)).strftime("%Y %m %d")
file.close()