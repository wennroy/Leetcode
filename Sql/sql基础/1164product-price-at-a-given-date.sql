#我这里由于newprice是原表里的，在LEFT JOIN时不会产生空值，因此查询max_date是空的。

# Write your MySQL query statement below
SELECT DISTINCT p.product_id, IF(t.max_date IS NULL, 10, p.new_price) price FROM Products p
LEFT JOIN(
    SELECT product_id, MAX(change_date) max_date FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
) AS t
ON p.product_id = t.product_id
WHERE t.max_date = p.change_date OR t.max_date IS NULL;


# 官方是找到是null的new_price
select p1.product_id, ifnull(p2.new_price, 10) as price
from (
    select distinct product_id
    from products
) as p1 -- 所有的产品
left join (
    select product_id, new_price
    from products
    where (product_id, change_date) in (
        select product_id, max(change_date)
        from products
        where change_date <= '2019-08-16'
        group by product_id
    )
) as p2 -- 在 2019-08-16 之前有过修改的产品和最新的价格
on p1.product_id = p2.product_id

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/product-price-at-a-given-date/solution/zhi-ding-ri-qi-de-chan-pin-jie-ge-by-leetcode-solu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。