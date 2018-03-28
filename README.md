# dw_dimention: for hive
## 1. d_date
```
date_proxy_key  date_key1   date_key2    full_date    date_name   day_of_week  day_of_month   day_of_year  week_of_year week_en_name  week_cn_name  month_of_year  month_cn_name  month_en_name   year_name  quarter_of_year  quarter_cn_name  quarter_en_name  calendar_year_month  calendar_year_quarter
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
date_proxy_key          String comment '代理主键',
date_key1               String comment '主键1',
date_key2               String comment '主键2',
full_date               Date   comment '日期的内容',
data_name               String comment '日期的名字',
day_of_week             Int    comment '每周第几天: 0~6',
day_of_month            Int    comment '每月第几天: 0~30',
day_of_year             Int    comment '每年第几天: 0~365',
week_of_year            Int    comment '每年第几周: 0~53',
week_en_name            String comment '周的英文名字',
week_cn_name            String comment '周的中文名字',
month_of_year           Int    comment '每年第几个月: 1~12',
month_cn_name           String comment '月的中文名字',
month_en_name           String comment '月的英文名字',
year_name               String comment '年的名字',
quarter_of_year         String comment '每年第一个季度: 1~4',
quarter_cn_name         String comment '季度中文名字',
quarter_en_name         String comment '季度英文名字',
calendar_year_month     String comment '年-月标识',
calendar_year_quarter   String comment '年季度标识'
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