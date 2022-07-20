# Write your MySQL query statement below
SELECT DISTINCT s.seller_name SELLER_NAME FROM Orders o
RIGHT JOIN Seller s
ON o.seller_id = s.seller_id
WHERE s.seller_id NOT in (
    SELECT seller_id FROM Orders
    WHERE sale_date between '2020-01-01' AND '2020-12-31'
)
ORDER BY SELLER_NAME;

# “2020年”的11种写法
# YEAR(sale_date) = 2020
# sale_date LIKE '2020%'
# sale_date REGEXP '^2020'
# LEFT(sale_date,4) = '2020'
# MID(sale_date,1,4) = '2020'
# SUBSTR(sale_date,1,4) = '2020'
# DATE_FORMAT(sale_date,'%Y') = 2020
# EXTRACT(YEAR FROM sale_date) = 2020
# sale_date BETWEEN '2020-01-01' AND '2020-12-31'
# sale_date > '2019-12-31' AND sale_date < '2021-01-01'
# sale_date >= '2020-01-01' AND sale_date <= '2020-12-31'
#
# 作者：richard-95
# 链接：https://leetcode.cn/problems/sellers-with-no-sales/solution/3chong-jie-fa-not-in-is-null-group_concat-by-richa/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。