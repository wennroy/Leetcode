# Write your MySQL query statement below
SELECT o.order_id FROM OrdersDetails o
GROUP BY o.order_id
HAVING max(o.quantity) > ALL(
    SELECT SUM(quantity) / COUNT(quantity) avg_quantity FROM OrdersDetails
    GROUP BY order_id
);


select
    order_id
from (
    -- 每个订单的最大数量 > max(每个订单的平均数量)
    select
        *,
        max(quantity) > max(avg(quantity)) over() as flag
    from OrdersDetails
    group by order_id
) as base
where flag = 1

# 作者：feng-167
# 链接：https://leetcode.cn/problems/orders-with-maximum-quantity-above-average/solution/jian-dan-jie-fa-kai-chuang-han-shu-by-fe-4os5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。