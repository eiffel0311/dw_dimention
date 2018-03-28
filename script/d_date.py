# -*- coding: UTF-8 -*-
import os
import datetime
from datetime import timedelta

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

def  get_full_date(arg1):
    return arg1.strftime("%Y-%m-%d")

def  get_date_name(arg1):
    return arg1.strftime("%Y-%m-%d")

def get_day_of_week(arg1):
    return arg1.strftime("%w")

def get_day_of_month(arg1):
    return bytes(int(arg1.strftime("%d")))

def get_day_of_year(arg1):
    return bytes(int(arg1.strftime("%j")))

def get_week_of_year(arg1):
    return bytes(int(arg1.strftime("%U")))

def get_week_en_name(arg1):
    return arg1.strftime("%A")

def get_week_cn_name(arg1):
    map = {'Monday': '星期一', 'Tuesday': '星期二', 'Wednesday': '星期三', 'Thursday': '星期四', 'Friday':  '星期五', 'Saturday': '星期六', 'Sunday':'星期日'}
    return map[arg1.strftime("%A")]

def get_month_of_year(arg1):
    return bytes(int(arg1.strftime("%m")))

def get_month_cn_name(arg1):
    map = { 'January':'一月',
                   'February': '二月',
                   'March': '三月',
                   'April': '四月',
                    'May': '五月',
                    'June': '六月',
                    'July': '七月',
                    'August': '八月',
                     'September': '九月',
                    'October': '十月',
                    'November': '十一月',
                    'December': '十二月'}
    return map[arg1.strftime("%B")]

def get_month_en_name(arg1):
    return arg1.strftime("%B")

def get_year_name(arg1):
    return arg1.strftime("%Y")

def get_quarter_of_year(arg1):
    month =arg1.strftime("%m")
    if month in ['01', '02', '03']:
    	return '1'
    elif month in ['04', '05', '06']:
    	return  '2'
    elif month in ['07', '08', '09']:
               return '3'
    else:
               return '4'

def get_quarter_cn_name(arg1):
    month =arg1.strftime("%m")
    if month in ['01', '02', '03']:
    	return '第一季度'
    elif month in ['04', '05', '06']:
    	return  '第二季度'
    elif month in ['07', '08', '09']:
               return '第三季度'
    else:
               return '第四季度'

def get_quarter_en_name(arg1):
    month =arg1.strftime("%m")
    if month in ['01', '02', '03']:
    	return 'Q1'
    elif month in ['04', '05', '06']:
    	return  'Q2'
    elif month in ['07', '08', '09']:
               return 'Q3'
    else:
               return 'Q4'

def get_calendar_year_month(arg1):
      return arg1.strftime("%Y-%m") 

def get_calendar_year_quarter(arg1):
      return arg1.strftime("%Y-") + get_quarter_en_name(arg1)

# arg1 = datetime.datetime.strptime(flag, "%Y %m %d")
# print get_date_proxy_key(arg1)
# print get_date_key1(arg1)
# print get_date_key2(arg1)
# print get_full_date(arg1)
# print get_date_name(arg1)
# print get_day_of_week(arg1)
# print get_day_of_month(arg1)
# print get_day_of_year(arg1)
# print get_week_of_year(arg1)
# print get_week_en_name(arg1)
# print get_week_cn_name(arg1)
# print get_month_of_year(arg1)
# print get_month_cn_name(arg1)
# print get_month_en_name(arg1)
# print get_year_name(arg1)
# print get_quarter_of_year(arg1)
# print get_quarter_cn_name(arg1)
# print get_quarter_en_name(arg1)
# print get_calendar_year_month(arg1)
# print get_calendar_year_quarter(arg1)

while flag != end:
    flag = datetime.datetime.strptime(flag, "%Y %m %d")
    file.write(get_date_proxy_key(flag) + ' ' + get_date_key1(flag) + ' ' + get_date_key2(flag) + ' ' + get_full_date(flag) + ' ' + get_date_name(flag) + ' ' + get_day_of_week(flag) + ' ' + get_day_of_month(flag) + ' ' + get_day_of_year(flag) + ' ' + get_week_of_year(flag) + ' ' + get_week_en_name(flag) + ' ' + get_week_cn_name(flag) + ' ' + get_month_of_year(flag) + ' ' + get_month_cn_name(flag) + ' ' + get_month_en_name(flag) + ' ' + get_year_name(flag) + ' ' + get_quarter_of_year(flag) + ' ' + get_quarter_cn_name(flag) + ' ' + get_quarter_en_name(flag) + ' ' + get_calendar_year_month(flag) + ' ' + get_calendar_year_quarter(flag) +"\n")
    flag = (flag + timedelta(days = 1)).strftime("%Y %m %d")
file.close()