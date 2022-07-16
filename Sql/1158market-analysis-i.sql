# 无法找到ORDER数量为0的users

# Write your MySQL query statement below
SELECT u.user_id buyer_id, u.join_date, COUNT(o.order_id) orders_in_2019 FROM Users u
LEFT JOIN Orders o
ON u.user_id = o.buyer_id
WHERE DATEDIFF(order_date, '2019-01-01') >= 0 AND DATEDIFF('2019-12-31', order_date) >= 0
GROUP BY u.user_id
ORDER BY buyer_id;

# 标答：在计算出COUNT之后利用IFNULL来找到为NULL值得用户，最后添加0上去

select Users.user_id as buyer_id, join_date, ifnull(UserBuy.cnt, 0) as orders_in_2019
from Users
left join (
    select buyer_id, count(order_id) cnt
    from Orders
    where order_date between '2019-01-01' and '2019-12-31'
    group by buyer_id
) UserBuy
on Users.user_id = UserBuy.buyer_id