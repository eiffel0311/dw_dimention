# dw_dimention: for hive
## 1. d_date
```
date_proxy_key  date_key1   date_key2    full_date    data_name   day_of_week  day_of_month   day_of_year  week_of_year week_en_name  week_cn_name  month_of_year  month_cn_name  month_en_name   year_name  quarter_of_year  quarter_cn_name  quarter_en_name  calendar_year_month  calendar_year_quarter
20000101        2000_01_01  2000-01-01   2000-01-01   2000-01-01       1             1              1            1        Saturday        星期六         1              一月         January          2000          1              第一季度          Q1               2017-01                 2017Q1
```
### 1.1. cd script and run:
```
 python d_date.py
 ```
### 1.2  you will find file d_date.csv
### 1.3   create table:
```
create table d_date(
  date_proxy_key   String,
  date_key1        String,
  date_key2        String,
  year             String,
  month            String,
  day              String,
  quarter_name     String,
  day_name_of_week String
)
row format delimited
fields terminated by ' '
stored as textfile
```
###  1.4 load data:
```
load data local inpath '/data/warehouse/aif_test/d_date.csv' into table d_date;
```
## 2. d_time
```
time_proxy_key     date_key1      date_key2      year      month   day      quarter_name    day_name_of_week
115958          2000_01_01     2000-01-01      2000       01     01             Q1         Saturday
```