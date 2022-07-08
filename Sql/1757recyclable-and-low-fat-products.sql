# Write your MySQL query statement below
# 语法练习
USE leetcode;

SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y';

# !代表否定
SELECT product_id
FROM Products
WHERE !(low_fats = 'N' OR recyclable = 'N');

# 组合判定
SELECT product_id
FROM Products
WHERE (low_fats,recyclable) = ('Y', 'Y');

# <>不等于
SELECT product_id
FROM Products
WHERE (low_fats,recyclable) <> ('Y', 'N')
AND (low_fats,recyclable) <> ('N', 'Y')
AND (low_fats,recyclable) <> ('N', 'N');

# AND 也可以用 *
SELECT product_id
FROM Products
WHERE low_fats = 'N' * recyclable = 'N';

# CONCAT 可以连接结果
SELECT product_id
FROM Products
WHERE CONCAT(low_fats,recyclable) = 'YY';


