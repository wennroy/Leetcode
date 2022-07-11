# Write your MySQL query statement below
SELECT product_id, 'store1' store, store1 price FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' store, store2 price FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' store, store3 price FROM Products
WHERE store3 IS NOT NULL;

# UNION ALL
select  product_id,
        'store1' as store,
        store1 as price
from    Products
where   store1 is not null
union all
select  product_id,
        'store2' as store,
        store2 as price
from    Products
where   store2 is not null
union all
select  product_id,
        'store3' as store,
        store3 as price
from    Products
where   store3 is not null

## 总结：UNION ALL 与 UNION 的区别：
# UNION ALL 保留每个原始数据集中的所有记录，UNION 删除任何重复记录。
# UNION 首先执行排序操作并消除所有列中重复的记录，然后最终返回组合数据集。