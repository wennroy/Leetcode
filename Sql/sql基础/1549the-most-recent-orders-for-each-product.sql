# Write your MySQL query statement below
SELECT p.product_name, o.product_id, o.order_id, o.order_date FROM Orders o
LEFT JOIN Products p
ON p.product_id = o.product_id
WHERE (o.order_date, o.product_id) IN (
    SELECT max(order_date) max_order_date, product_id FROM Orders
    GROUP BY product_id
)
ORDER BY p.product_name, o.product_id, o.order_id;

# 一般认为能少用IN则尽可能少用IN，选用WHERE EXISTS来代替，由于图片挂了，不太懂讲了啥= =
SELECT
    t1.product_name,
    t2.product_id,
    t2.order_id,
    t2.order_date
FROM
    Products AS t1
INNER JOIN Orders AS t2 ON t1.product_id = t2.product_id
WHERE EXISTS (
    SELECT
        product_id,
        MAX(order_date) AS 'last_order_date'
    FROM
        Orders AS t3
    GROUP BY product_id
    HAVING t1.product_id = t3.product_id AND t2.order_date = last_order_date
)
ORDER BY t1.product_name, t2.product_id, t2.order_id

# 作者：13rtk
# 链接：https://leetcode.cn/problems/the-most-recent-orders-for-each-product/solution/inyu-existsde-fen-xi-sqlyou-hua-by-13rtk-mhbk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。