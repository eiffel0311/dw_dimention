# dw_dimention: for hive
## 1. d_date
```
* date_proxy_key     date_key1      date_key2        
* 20000101           2000_01_01     2000-01-01
	** full_date    date_name 
	** 2000-01-01   2000/01/01
        *** day_of_week    day_en_name_of_week     day_cn_name_of_week       day_of_month                          year      month   day      quarter_name    day_name_of_week                              
        ***  2000-01-01    2000/01/01    
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