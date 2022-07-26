# Mysql

## Mysql常用语句查询
https://www.w3schools.com/mysql

mysql是怎样陨星的：
https://relph1119.github.io/mysql-learning-notes/

## Mysql REGEXP的运用
https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/
https://www.runoob.com/mysql/mysql-regexp.html

## COALESCE()函数的运用
https://www.w3schools.com/sql/func_mysql_coalesce.asp

Return the first non-null value in a list:

```mysql
COALESCE(val1, val2, ...., val_n);
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

## WINDOWN FUNCTION
https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html

### OVER（）
```mysql
[你要的操作] OVER ( PARTITION BY  <用于分组的列名>
                    ORDER BY <按序叠加的列名> 
                    ROWS <窗口滑动的数据范围> )
```
Partition by 和 order by很直观，这里主要注重ROWS的操作。ROWS同时也可以换成RANGE，并且有时更加方便。

<窗口滑动的数据范围> 用来限定[你要的操作] 所运用的数据的范围，具体有如下这些：
```mysql
当前行 - current row
之前的行 - preceding
之后的行 - following
无界限 - unbounded
表示从前面的起点 - unbounded preceding
表示到后面的终点 - unbounded following
```
举例理解一下就是：
```mysql
取当前行和前五行：ROWS between 5 preceding and current row --共6行
取当前行和后五行：ROWS between current row and 5 following --共6行
取前五行和后五行：ROWS between 5 preceding and 5 folowing --共11行
```
对于滑动窗口前后行的选取，例题之一：[1321. 餐馆营业额变化增长](https://leetcode.cn/problems/restaurant-growth/)([题解笔记](https://github.com/wennroy/Leetcode/blob/master/Sql/sql%E5%9F%BA%E7%A1%80/1321restaurant-growth.sql))

### ROW_NUMBER()
https://www.mysqltutorial.org/mysql-window-functions/mysql-row_number-function/

返回当前筛选出的表的行数。
```mysql
ROW_NUMBER() OVER (<partition_definition> <order_definition>);
```
