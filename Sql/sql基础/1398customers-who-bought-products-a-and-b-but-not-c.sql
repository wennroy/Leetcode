# 简单的Having SUM
# Write your MySQL query statement below
SELECT Orders.customer_id, customer_name FROM Orders, Customers
WHERE Orders.customer_id = Customers.customer_id
GROUP BY customer_id
HAVING SUM(IF(product_name='A', 1, 0)) <> 0 AND SUM(IF(product_name='B', 1, 0)) <> 0 AND SUM(IF(product_name='C', 1, 0)) = 0


# GROUP_CONCAT 和 REGEXP
select customer_id, customer_name
from Customers
where customer_id in (
select
	customer_id
from Orders
group by customer_id
having
	group_concat(distinct product_name) REGEXP '^A,B$|^A,B,[^C].*'
)

# 作者：vigilant-dubinskyiwo
# 链接：https://leetcode.cn/problems/customers-who-bought-products-a-and-b-but-not-c/solution/group_concat-by-vigilant-dubinskyiwo-6wq1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。