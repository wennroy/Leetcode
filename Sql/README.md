# Mysql

## Mysql常用语句查询
https://www.w3schools.com/mysql

## Mysql REGEXP的运用
https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/
https://www.runoob.com/mysql/mysql-regexp.html

## COALESCE()函数的运用
https://www.w3schools.com/sql/func_mysql_coalesce.asp

Return the first non-null value in a list:

```mysql
COALESCE(val1, val2, ...., val_n)
```

## 时间判断的各种写法

“2020年”的11种写法
```mysql
# YEAR(sale_date) = 2020
sale_date LIKE '2020%'
sale_date REGEXP '^2020'
LEFT(sale_date,4) = '2020'
MID(sale_date,1,4) = '2020'
SUBSTR(sale_date,1,4) = '2020'
DATE_FORMAT(sale_date,'%Y') = 2020
EXTRACT(YEAR FROM sale_date) = 2020
sale_date BETWEEN '2020-01-01' AND '2020-12-31'
sale_date > '2019-12-31' AND sale_date < '2021-01-01'
sale_date >= '2020-01-01' AND sale_date <= '2020-12-31'
```
