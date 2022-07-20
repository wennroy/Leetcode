# Write your MySQL query statement below
SELECT ROUND(COUNT(IF(order_date = customer_pref_delivery_date, 1, NULL)) / (SELECT COUNT(1) FROM Delivery) * 100,
             2) immediate_percentage
FROM Delivery;

# SUM方便计算
select round (
    sum(order_date = customer_pref_delivery_date) /
    count(*) * 100,
    2
) as immediate_percentage
from Delivery

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/immediate-food-delivery-i/solution/ji-shi-shi-wu-pei-song-i-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。