# Write your MySQL query statement below
with temp as(
SELECT DISTINCT customer_id, c.product_key FROM Customer c
)
SELECT t.customer_id FROM temp t
GROUP BY t.customer_id
HAVING SUM(t.product_key) = (
    SELECT SUM(p.product_key) sum_product_key FROM Product p
);

# 利用COUNT方法
# Write your MySQL query statement below
SELECT
    customer_id
FROM
    customer
GROUP BY customer_id
HAVING count(DISTINCT product_key) = (
    SELECT
        count(DISTINCT product_key)
    FROM product
);

# 作者：Jam007
# 链接：https://leetcode.cn/problems/customers-who-bought-all-products/solution/by-jam007-evg4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

SELECT
    t1.customer_id
FROM
    Customer AS t1
INNER JOIN Product AS t2 ON t1.product_key = t2.product_key
GROUP BY t1.customer_id
HAVING COUNT(DISTINCT t2.product_key) = (SELECT COUNT(*) FROM Product)

# 作者：13rtk
# 链接：https://leetcode.cn/problems/customers-who-bought-all-products/solution/by-13rtk-i1g1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。