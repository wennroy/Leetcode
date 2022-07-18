# 少了个DISTINCT，没有DISTINCT的话，我们会有多条符合条件的数据，将会重复显示
# Write your MySQL query statement below
SELECT DISTINCT p.product_id, p.product_name FROM Product p, Sales s
WHERE p.product_id = s.product_id AND s.product_id NOT IN
(
SELECT product_id FROM Sales
WHERE DATEDIFF(sale_date, '2019-01-01') < 0 OR DATEDIFF(sale_date, '2019-03-31') > 0
);

# 大佬总能给我整出点新活 GROUP BY之后计算COUNT是否相等
# Write your MySQL query statement below
select p.product_id, p.product_name
from Product p, Sales s
where p.product_id = s.product_id
group by s.product_id
having(sum(sale_date between '2019-01-01' and '2019.03-31') = count(*));

# 作者：kobe24o
# 链接：https://leetcode.cn/problems/sales-analysis-iii/solution/havingsumsale_date-between-2019-01-01-and-201903-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 用GROUP BY 效率尚可
# Write your MySQL query statement below
SELECT
    s.product_id, p.product_name
FROM
    sales s
LEFT JOIN
    product p
ON
    s.product_id = p.product_id
GROUP BY
    s.product_id
HAVING MIN(sale_date) >= '2019-01-01'
AND MAX(sale_date) <= '2019-03-31';

# 作者：Jam007
# 链接：https://leetcode.cn/problems/sales-analysis-iii/solution/by-jam007-z0wa/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。