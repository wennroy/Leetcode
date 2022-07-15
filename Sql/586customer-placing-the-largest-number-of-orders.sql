# 超复杂且无语的写法emmm
# Write your MySQL query statement below
SELECT DISTINCT o1.customer_number FROM Orders o1
INNER JOIN (SELECT customer_number, COUNT(order_number) order_count FROM Orders
GROUP BY customer_number
ORDER BY order_count DESC
LIMIT 1) o2
ON o1.customer_number = o2.customer_number;

# 标答，利用GROUP BY 和 COUNT(*) 来解释
# COUNT(*) The COUNT(*) function returns the number of rows in a dataset using the SELECT statement.
SELECT
    customer_number
FROM
    orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
;

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/customer-placing-the-largest-number-of-orders/solution/ding-dan-zui-duo-de-ke-hu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 子语句也是可行的

select customer_number
from
(
    select customer_number,count(order_number) as order_num
    from orders
    group by customer_number
    order by order_num desc
) t
limit 1;