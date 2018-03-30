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
time_proxy_key  time_24hour_key  hour_of_day_24 hour_of_day_12  am_pm   minute_of_hour  half_hour half_hour_of_day quarter_hour quarter_hour_of_day string_representation_24 string_representation_12 
0                 24:00:00            0              12          AM         0               1~2         1~48         1~4            1~96                  00:00                    12:00 
```
### 2.1. cd script and run:
```
 python d_time.py
 ```
### 2.2  you will find file d_time.csv
### 2.3   create table:
```
create table d_time(
time_proxy_key            Int       comment '时间维度代理主键: 0~1439',
time_24hour_key           String    comment '主键',
hour_of_day_24            Int       comment '24时计时法: 0~23',
hour_of_day_12            String    comment '12时计时法: 0~11',
am_pm                     String    comment 'AM or PM',
minute_of_hour            Int       comment '每小时的第几分钟: 0~59',
half_hour                 Int       comment '把一小时分两份: 1~2',
half_hour_of_day          Int       comment '把一小时分两份: 1~24',
quarter_hour              Int       comment '把一小时分四份: 1~4',
quarter_hour_of_day       Int       comment '把一小时分四份: 1~96',
string_representation_24  String    comment '24时计时法字符串表示',
string_representation_12  String    comment '12时计时法字符串表示'
)
row format delimited
fields terminated by ' '
stored as textfile
```
###  2.4 load data:
```
load data local inpath '/data/warehouse/aif_test/d_time.csv' into table d_time;
```

## 3. d_region_city
```
region_city_proxy_key	city_name_key	  city_id  	city_cn_name	province_id 	porvince_cn_name
110000                       北京市	     110000	    北京市	           110000	      北京市
```
### 3.1   create table:
```
create table d_region_city(
region_city_proxy_key  String comment '城市维度代理主键',
city_name_key	       String comment '主键:城市名字',
city_id                String comment '六位城市ID',
city_cn_name           String comment '城市中文名',
province_id            String comment '六位省份ID, 引用d_region_province.region_province_proxy_key',
porvince_cn_name       String comment '城市中文名字'
)
row format delimited
fields terminated by ' '
stored as textfile
```
###  3.2 load data, find file d_region_city.csv in directory dementions, for details: http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/
```
load data local inpath '/data/warehouse/aif_test/d_region_city.csv' into table d_region_city;
```
## 4. d_region_province
```
region_province_proxy_key  province_key province_name    province_id   province_for_short  region_name  region_id
110000                     北京市            北京市        110000        BJ                  华北             1
```
### 4.1   create table:
```
create table d_region_province(
region_province_proxy_key  String comment '省份维度代理主键',
province_key	           String comment '主键:省份名字',
province_name              String comment '省份名称',
province_id                String comment '六位省份ID',
province_for_short         String comment '省份简写',
region_name                String comment '大区名字:1:华北,2:东北,3:华东,4:中南,5:西南,6:西北,7:港澳台',
region_id                  String comment '大区ID:1:华北,2:东北,3:华东,4:中南,5:西南,6:西北,7:港澳台'  
)
row format delimited
fields terminated by ' '
stored as textfile
```
###  4.2 load data, find file d_region_province.csv in directory dementions
```
load data local inpath '/data/warehouse/aif_test/d_region_province.csv' into table d_region_province;
```
